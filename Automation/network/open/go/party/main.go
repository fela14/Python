package main

import (
	"fmt"
	log "github.com/sirupsen/logrus"
)

func main() {
	vlanIDs := []int {
		100,200,300
	}
	log.Infof("Hello from logrus! There are %d VLANs in the vlanIDs slice.", len(vlanIDs))
	fmt.Println("End of program")
}