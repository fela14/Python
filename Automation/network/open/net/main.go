package main

import (
    "bytes"
    "crypto/tls"
    "fmt"
    "io"
    "log"
    "net/http"
)

func checkError(err error) {
    if err != nil {
        log.Fatal(err)
    }
}

func basicAuth(username, password string) string {
    // simple Base64 encoder
    return fmt.Sprintf("%s:%s", username, password)
}

func main() {
    username := "developer"
    password := "C1sco12345"
    baseURL := "https://10.10.20.48/restconf/data/Cisco-IOS-XE-native:native"

    // Skip TLS certificate validation (sandbox uses self-signed cert)
    tr := &http.Transport{
        TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
    }
    client := &http.Client{Transport: tr}

    // --- First: Perform a GET request ---
    req, err := http.NewRequest("GET", baseURL, nil)
    checkError(err)
    req.SetBasicAuth(username, password)
    req.Header.Set("Accept", "application/yang-data+json")

    resp, err := client.Do(req)
    checkError(err)
    defer resp.Body.Close()

    body, err := io.ReadAll(resp.Body)
    checkError(err)
    fmt.Println("=== Current Device Configuration ===")
    fmt.Println(string(body))

    // --- Second: Perform a PUT request to update VLAN ---
    vlanURL := baseURL + "/vlan"
    jsonStr := []byte(`{
        "Cisco-IOS-XE-native:vlan": {
            "Cisco-IOS-XE-vlan:vlan-list": [
                {
                    "id": 20,
                    "name": "Updated_VLAN_20"
                }
            ]
        }
    }`)

    putReq, err := http.NewRequest("PUT", vlanURL, bytes.NewBuffer(jsonStr))
    checkError(err)
    putReq.SetBasicAuth(username, password)
    putReq.Header.Set("Accept", "application/yang-data+json")
    putReq.Header.Set("Content-Type", "application/yang-data+json")

    putResp, err := client.Do(putReq)
    checkError(err)
    defer putResp.Body.Close()

    putBody, err := io.ReadAll(putResp.Body)
    checkError(err)
    fmt.Println("=== VLAN Update Response ===")
    fmt.Println(string(putBody))
}
