package main

import (
	"encoding/csv"
	"fmt"
	"io"
	"log"
	"os"
	"strconv"

	"github.com/gonum/matrix/mat64"
)

var (
	dataPath = func() string {
		d, _ := os.Getwd()
		return d
	}() + "/data/generated/"
)

var dimension = 13

func readCSVData(rc io.Reader) (ch chan []string) {
	ch = make(chan []string, 10)
	go func() {
		r := csv.NewReader(rc)
		defer close(ch)
		for {
			rec, err := r.Read()
			if err != nil {
				if err == io.EOF {
					break
				}
				log.Fatal(err)
			}
			ch <- rec
		}
	}()
	return
}

func loadData() (*mat64.Dense, *mat64.Vector) {
	csvfile, _ := os.Open(dataPath + "1Y.csv")
	datas := []float64{}
	for line := range readCSVData(csvfile) {
		for _, val := range line {
			floatVal, _ := strconv.ParseFloat(val, 64)
			datas = append(datas, floatVal)
		}
	}

	datasCount := len(datas)
	matData := mat64.NewDense(datasCount/dimension, dimension, datas)
	r, c := matData.Dims()
	var features mat64.Dense
	features.Clone(matData.Slice(0, r, 0, c-1))

	return &features, matData.ColView(c - 1)
}

func main() {
	X, Y := loadData()
	weigth := mat64.NewVector(dimension-1, nil)
	numIteration := 100
	learningRate := 0.1

	for i := 0; i < numIteration; i++ {
		var pred mat64.Vector
		pred.MulVec(X, weigth)

		fmt.Println(pred.At(0, 0), Y.At(0, 0))

		var error mat64.Vector
		error.SubVec(&pred, Y)

		for j := 0; j < dimension-1; j++ {
			var grad mat64.Vector
			grad.MulElemVec(&error, X.ColView(j))
			sum := mat64.Sum(&grad)

			weigth.SetVec(j, weigth.At(j, 0)-(sum*learningRate))
		}
	}
}
