package main

import (
	"context"
	"fmt"
	"log"

	"github.com/openconfig/gnmic/api"
	"google.golang.org/protobuf/encoding/prototext"
)

// helper function for error checking
func checkError(err error) {
	if err != nil {
		log.Fatal(err)
	}
}

func main() {
	// Create a gNMI target (replace with your sandbox details)
	tg, err := api.NewTarget(
		api.Name("Cisco Sandbox gNMI Target"),
		api.Address("10.10.20.48:57400"), // <-- replace with actual IP and gNMI port from your sandbox
		api.Username("admin"),            // <-- use sandbox username
		api.Password("C1sco12345"),        // <-- use sandbox password
		api.Insecure(true),               // disable TLS for DevNet
	)
	checkError(err)

	// cancelable context
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	// create gNMI client
	err = tg.CreateGNMIClient(ctx)
	checkError(err)
	defer tg.Close()

	// First GetRequest - full state
	getReq, err := api.NewGetRequest(
		api.Path("/"),             // get everything
		api.Encoding("json_ietf"), // request JSON IETF encoding
	)
	checkError(err)

	getResp, err := tg.Get(ctx, getReq)
	checkError(err)

	// Pretty-print first response
	out, err := prototext.Marshal(getResp)
	checkError(err)
	fmt.Println("=== Full Device State ===")
	fmt.Println(string(out))

	// Second GetRequest - only interface config
	getReq, err = api.NewGetRequest(
		api.Path("/interfaces/interface/config"),
		api.Encoding("json_ietf"),
	)
	checkError(err)

	getResp, err = tg.Get(ctx, getReq)
	checkError(err)

	// Pretty-print second response
	out, err = prototext.Marshal(getResp)
	checkError(err)
	fmt.Println("=== Interface Config ===")
	fmt.Println(string(out))

	newDescription := "hello"
	setReq, err := api.NewSetRequest(
		api.Update(
			path.ToGNMIPath("")
			value.String(newDescription)
		)
	)
	checkError(err)

	setResp, err := tg.Set(ctx, setReq)
	checkError(err)

	out, err := io.ReadAll(setResp)
	
}
