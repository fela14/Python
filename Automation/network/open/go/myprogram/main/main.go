package main

import (
	"errors"
	"fmt"
	"math"
	"net"
	"os"
	"regexp"
	"strconv"
	"strings"

	// "sync" // Concurrency
	"encoding/json"
	"encoding/xml"
	"myprogram/devices"
	"myprogram/generator"
	"myprogram/ssot"
	"time"

	//"net/http"
	"net/netip"
)

func main() {
	fmt.Println("Hello, network automators!")

	var myString1 string = "Hello, network gophers!"
	// var myStrin2 string
	var myString3 = "Hello, network gophers!"
	myString4 := "Hello!"
	var (
		myString5 string
		myString6 = "Hello, network gophers!"
	)
	fmt.Println(myString1, myString3, myString4, myString5, myString6, '\n')

	const myString7 string = "Hello network gophers"
	// myString7 = "new value"
	const Pi = 3.14
	const (
		myString8 = "Hello, go"
		retries   = 3
	)
	fmt.Println(myString7, myString8, Pi, retries)

	var snmpConfigured bool = false
	if snmpConfigured {
		println("SNMP is configured")
	} else {
		println("SNMP is not configured")
	}

	var vlanID int = 102
	if vlanID < 100 {
		fmt.Println("VLAN ID is less than 100")
	} else if vlanID > 100 && vlanID < 1000 {
		fmt.Println("VLAN ID is between 100 and 1000")
	} else {
		fmt.Println("VLAN ID is greater than 1000")
	}

	// Simple loop that prints VLAN IDs in order from 1-5. It
	// accomplishes this by incrementing a counter
	// and exits once it's greater than 5
	i := 1
	for i <= 5 {
		fmt.Printf("VLAN is %d\n", i)
		i += 1
	}
	for b := 1; b <= 5; b++ {
		fmt.Printf("Vlan is %d\n", b)
	}

	// We can use the continue keyword to cause the loop to repeat
	// earlier than it normally would
	for i := 1; i <= 5; i++ {
		if i == 3 {
			continue
		}
		// Because of the continue statement above,
		// this line will not run when i == 3
		fmt.Printf("VLAN %d\n", i)
	}

	vlanID = 1
	for {
		fmt.Printf("Looking at VLAN %d\n", vlanID)
		if vlanID > 5 {
			break
		}
		vlanID++
	}

	// This declares "vlans" as an array of type "int"
	// and a size of 3.
	var vlans [3]int
	// Once initialized, we can set values in the array
	// by their index. Since arrays have a fixed size,
	// the compiler can warn us if we use an invalid index
	//
	// Don't forget, slices and arrays start with index 0!
	vlans[0] = 1
	// You can also initialize arrays with values at
	// the same time

	fmt.Println(vlans)
	vlans2 := [3]int{1, 2, 3}
	fmt.Println(vlans2)

	// var intSlice []int
	// var stringSlice []string
	var vlanSlice = []int{11, 22, 33, 44, 55}
	vlanSlice2 := []int{66, 77, 88, 99}
	fmt.Println(vlanSlice, vlanSlice2)
	vlanSlice = append(vlanSlice, 100)
	fmt.Println(vlanSlice)

	vlanSlice = []int{3, 5, 7}
	fmt.Println(cap(vlanSlice), len(vlanSlice))
	vlanSlice = append(vlanSlice, 200)
	fmt.Printf("vlanSlice cap is %d, len is %d\n", cap(vlanSlice), len(vlanSlice))

	preallocatedvlanSlice := make([]int, 2, 50)
	fmt.Printf("vlanSlice cap is %d, len is %d\n", cap(preallocatedvlanSlice), len(preallocatedvlanSlice))

	preallocatedvlanSlice[0] = 1
	preallocatedvlanSlice[1] = 2

	for i := 3; i <= 50; i++ {
		preallocatedvlanSlice = append(preallocatedvlanSlice, i)
	}
	// output: preallocatedVlanSlice1 cap is 50, len is 50
	fmt.Printf("preallocatedVlanSlice cap is %d, len is %d\n", cap(preallocatedvlanSlice), len(preallocatedvlanSlice))

	vlanSliceiter := []int{11, 22, 33, 44, 55, 66, 77, 88, 99}

	for i := 0; i < len(vlanSliceiter); i++ {
		fmt.Printf("Vlan slice iter index %d has a value of %d\n", i, vlanSliceiter[i])
	}

	for i := range vlanSliceiter {
		fmt.Printf("Vlan slice iter index %d has a value of %d\n", i, vlanSliceiter[i])
	}

	for i, val := range vlanSliceiter {
		fmt.Printf("Vlan slice iter index %d has a value of %d\n", i, val)

	}

	toFind := 33

	for i, val := range vlanSliceiter {
		if val == toFind {
			fmt.Printf("Found! Index is %d\n", i)
			break
		}
	}

	/* deviceloop:
		for _, device := range devices {
			for i, iface := range device.interfaces {
				for _, vlanID := range iface.vlans {
					if vlanID == 400 {
						fmt.Printf("Device %s has vlan 400 configured on interface %d\n", device.hostname, i)
						break deviceloop
					}
				}
			}
		}
	} */

	// var nilMap map[string]int
	// nilMap["foo"] = 80

	// var myMap = make(map[string]int)
	// var myMap2 = map[string]int{}
	// myMap3 := map[string]int{}

	vlanMap := map[string]int{
		"VLAN_100": 100,
		"VLAN_200": 200,
		"VLAN_300": 300,
	}
	vlan := vlanMap["VLAN_300"]
	fmt.Printf("vlan is %d\n", vlan)

	vlanMap["VLAN_400"] = 400
	vlanMap["VLAN_500"] = 500

	delete(vlanMap, "VLAN_300")
	fmt.Println(vlanMap)

	fmt.Println((vlanMap["VLAN_999"]))

	if val, found := vlanMap["VLAN_999"]; found {
		fmt.Printf("Found vlan %d", val)
	}

	if _, found := vlanMap["VLAN_999"]; !found {
		fmt.Printf("Not found in the map\n")
	}

	if val, found := vlanMap["VLAN_400"]; found {
		fmt.Printf("Found vlan %d\n", val)
	}

	for key, value := range vlanMap {
		fmt.Printf("%s has a value of %d\n", key, value)
	}

	for key := range vlanMap {
		fmt.Printf("Found key %s\n", key)
	}

	//doPrint()
	printMessage("go")
	totalIPv4Addresses(10)
	fmt.Println(sumAndProduct(2, 4))
	fmt.Println(createVlan(5000))
	fmt.Println(NewVlan(500, "HELLO"))

	myVlan1 := vlan1{
		id:   1,
		name: "VLAN_1",
	}
	myVlan1.id = 2
	myVlan1.name = "VLAN_2"
	fmt.Println(myVlan1)

	myDevice := device{
		hostname: "switch1",
		//vlans:    []vlan1{1, 2, 3},
	}
	myDevice.printHostname()
	myDevice.setHostname("r1")
	myDevice.printHostname()

	// rtr = Router{hostname: "rtr1-dc1"}
	// printHostnameTrimmed(rtr, 4)

	// Concurrency

	/* time.Sleep(1 * time.Second)
	go time.Sleep(10 * time.Second)

	var wg sync.WaitGroup
	var numGoroutines = 5

	wg.Add(numGoroutines)

	for i := 1; i <= numGoroutines; i++ {
		go func(i int) {
			defer wg.Done()
			fmt.Printf("Goroutine started with duration of %d seconds\n", i)
			time.Sleep(time.Duration(i) * time.Second)
			fmt.Printf("%d second goroutine finished!\n", i)
		}(i)
	}

	wg.Wait()
	fmt.Println("Program finished!") */

	// Generics

	fmt.Println(Min(2, 3))
	fmt.Println(Min(20.3, 5.43))
	fmt.Println(Min("Go", "Lang"))

	exampleString := `
	Hello network automators! Welcome to Network Programmability and Automation.
	`
	fmt.Println(exampleString)

	doesContain := strings.Contains(exampleString, "Automation")
	fmt.Println(doesContain)

	substringIndex := strings.Index(exampleString, "Welcome")
	fmt.Println(substringIndex)

	strSplit := strings.Split(exampleString, " ")
	fmt.Println(strSplit)
	fmt.Println(strSplit[4:])

	strJoin := strings.Join(strSplit, "*")
	fmt.Println(strJoin)

	strTrimmed := strings.TrimSpace("     Automation!")
	fmt.Println(strTrimmed)

	strReplace := strings.ReplaceAll(exampleString, "network", "gopher")
	fmt.Println(strReplace)

	i, err := strconv.Atoi("-42")
	if err != nil {
		fmt.Printf("Cannot convert string to int %d\n", err)
	} else {
		fmt.Printf("Converted to %d\n", i)
	}

	i42 := strconv.Itoa(42)
	fmt.Printf("i42 converted to string is %s\n", i42)

	outputStr := `
		eth0: flags=4099<UP,BROADCAST,MULTICAST> mtu 1500
		inet 172.17.0.1 netmask 255.255.0.0 broadcast 172.17.255.255
		ether 02:12:2a:24:5b:98 txqueuelen 0 (Ethernet)
	`
	re, err := regexp.Compile(`([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}`)
	if err != nil {
		panic(err)
	}
	fmt.Println(re.MatchString(outputStr))
	fmt.Println(re.FindString(outputStr))
	fmt.Println(re.ReplaceAllString(outputStr, "00:00:00:00:00:00"))

	// Interfaces

	// Create devices
	r := Router{hostname: "MainRouter", vrfs: []string{"VRF1", "VRF2"}}
	s := Switch{hostname: "CoreSwitch", vlans: []string{"10", "20"}}
	f := Firewall{hostname: "EdgeFW", zones: []string{"DMZ", "LAN"}}

	// Using concrete function
	printHostname(r)

	// Using interface functions
	fmt.Println("Switch hostname via interface:", s.getHostname())
	fmt.Println("Firewall hostname via interface:", f.getHostname())

	// Using Trimmable interface
	printHostnameTrimmed(&r, 4) // pass pointer because TrimHostname has pointer receiver

	// from package devices

	generator.NumberGenerate(5.5, 6.6)
	devices.PrintDevices("cisco\n")
	fmt.Println(ssot.NewSSOT("Standby\n"))

	r1 := Device{
		Hostname: "r1",
		Interfaces: []NetworkInterface{
			{
				Name:  "eth0",
				Speed: 1000,
			},
		},
	}

	jsonOut, err := json.Marshal(&r1)
	if err != nil {
		panic(err)
	}
	fmt.Println(string(jsonOut))

	xmlOut, err := xml.Marshal(&r1)
	if err != nil {
		panic(err)
	}
	fmt.Println(string(xmlOut))

	// Querying an HTTP API with net/http package

	/* resp, err := http.Get("https://api.ipify.org?format=json")
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}
	ipifyResponse := struct {
		IP string `json:"Ip"`
	}{}
	err = json.Unmarshall(body, &ipifyResponse)
	if err != nil {
		panic(err)
	}
	fmt.Println(ipifyResponse.IP)

	client := &http.Client{}

	req, err := http.NewRequest("GET", "https://api.ipify.org?format=json", nil)
	if err != nil {
		panic(err)
	}
	req.Header.Add("My-Header", `foo`)
	resp, err = client.Do(req)
	*/

	var ipFromByteSlice net.IP = []byte{192, 168, 0, 1}
	fmt.Println(ipFromByteSlice)

	var newIp net.IP = []byte{192, 168, 10, 1}
	fmt.Println(newIp)

	addrOne := net.ParseIP("172.16.10.10")
	addrTwo := net.ParseIP("172.16.20.20")
	fmt.Println(addrOne)
	fmt.Println(addrTwo)

	network := net.IPNet{
		IP:   net.ParseIP("172.16.10.0"),
		Mask: net.CIDRMask(24, 32),
	}

	fmt.Println(network.Contains(addrOne))
	fmt.Println(network.Contains(addrTwo))

	another_network := net.IPNet{
		IP:   net.ParseIP("172.16.20.0"),
		Mask: net.CIDRMask(24, 32),
	}

	fmt.Println(another_network.Contains(addrOne))
	fmt.Println(another_network.Contains(addrTwo))

	// The net/netip package

	ipv6, err := netip.ParseAddr("2001:db8::1")
	if err != nil {
		panic(err)
	}
	fmt.Println(ipv6.IsGlobalUnicast())

	fmt.Println(netip.AddrFrom4([4]byte{127, 0, 0, 1}).IsLoopback())
	fmt.Println(netip.AddrFrom4([4]byte{197, 0, 0, 2}).IsLoopback())

	prefixString := "192.168.0.0/24"
	prefix, err := netip.ParsePrefix(prefixString)
	if err != nil {
		panic(err)
	}
	fmt.Println(prefix)

	// Time

	now := time.Now
	fmt.Println(now)

	moonLanding := time.Date(1969, time.July, 20, 20, 17, 45, 0, time.UTC)
	fmt.Println(moonLanding)

	var oneSecond time.Duration = 1000000000
	fmt.Println(oneSecond)

	tenSecond := 10 * time.Second
	fmt.Println(tenSecond)

	fmt.Println(time.Since(moonLanding))

	// os package
	dat, err := os.ReadFile("../../files/sample.yaml")
	if err != nil {
		panic(err)
	}
	fmt.Println(string(dat))

	jsonOut1, err := json.Marshal(struct {
		Hostname   string
		Interfaces []string
	}{
		"sw01",
		[]string{"eth0", "eth1", "eth2"},
	})
	if err != nil {
		panic(err)
	}
	err = os.WriteFile("../../files/sample2.json", jsonOut1, 0644)
	if err != nil {
		fmt.Printf("Unable to write file: %s\n", err)
		os.Exit(1)
	}

	jsonOut2, err := json.Marshal(struct {
		Hostname   string
		Interfaces []string
	}{
		"switch1",
		[]string{"vlan1", "vlan2", "vlan3"},
	})
	if err != nil {
		panic(err)
	}
	err = os.WriteFile("../../files/file.json", jsonOut2, 0644)
	if err != nil {
		fmt.Printf("Could not write file %s\n", err)
		os.Exit(1)

	}
	// Signals
	/* sigs := make(chan os.Signal, 1)
	signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM)
	go func() {
		for {
			fmt.Println("Doing some work...")
			time.sleep(1 * time.Second)
		}
	}()

	<-sigs

	fmt.Println("exiting")
	os.Exit(0) */

	doPrint()

	

}

func doPrint() {
	fmt.Println("Hello network automators!")
	fmt.Println("Welcome to Network Programmability and Automation!")
	fmt.Println("Enjoy this chapter on the Go programming language.")

}
func printMessage(msg string) {
	fmt.Printf("Hello guys, we are learning %s today\n", msg)
}

func totalIPv4Addresses(prefixLen int) {
	x := 32 - prefixLen
	addrCount := math.Pow(2.0, float64(x))
	fmt.Printf("There are %d addresses in a /%d prefix\n", addrCount, prefixLen)
}

func sumAndProduct(a, b int) (int, int) {
	sum := a + b
	product := a * b
	return sum, product
}

func createVlan(id int) error {
	if id >= 4096 {
		return errors.New("Cannot create vlans above 4096")
	}
	fmt.Printf("Creating vlan %d\n", id)
	return nil
}

/*
	 func returnFromNestedLoops() {
		for _, device := range devices {
			for i, iface := range device.interfaces {
				for _, vlanID := range iface.vlans {
					if vlanID == 400 {
						fmt.Printf("Device %s has vlan 400 configured on interface %d\n", device.hostname, i)
						return
					}
				}
			}
		}
	}
*/

type vlan1 struct {
	id   uint
	name string
}

func NewVlan(id uint, name string) (vlan1, error) {
	if id >= 4096 {
		return vlan1{}, errors.New("Cannot create vlan >= 4096")
	}
	return vlan1{
		id,
		name,
	}, nil
}

type device struct {
	hostname string
	vlans    []vlan1
}

func (d device) printHostname() {
	fmt.Printf("Hostname is %s\n", d.hostname)
}

func (d *device) setHostname(hostname string) {
	if len(hostname) > 10 {
		hostname = hostname[:10]
	}
	d.hostname = hostname
	fmt.Println(d.hostname)
}

// Interfaces
// Trimmable interface requires two methods
type Trimmable interface {
	TrimHostname(int)
	getHostname() string
}

// Hostnamer interface requires only getHostname
type Hostnamer interface {
	getHostname() string
}

// Router struct
type Router struct {
	hostname string
	vrfs     []string
}

// Switch struct
type Switch struct {
	hostname string
	vlans    []string
}

// Firewall struct
type Firewall struct {
	hostname string
	zones    []string
}

// Implement getHostname for Switch
func (s Switch) getHostname() string {
	return fmt.Sprintf("Switch-%s", s.hostname)
}

// Implement getHostname for Firewall
func (f Firewall) getHostname() string {
	return fmt.Sprintf("Firewall-%s", f.hostname)
}

// Print router hostname (without interface)
func printHostname(device Router) {
	fmt.Printf("hostname is %s\n", device.hostname)
}

// Implement getHostname for Router
func (r Router) getHostname() string {
	return r.hostname
}

// Implement TrimHostname for Router
func (r *Router) TrimHostname(length int) {
	if len(r.hostname) > length {
		r.hostname = r.hostname[:length]
	}
}

// Print trimmed hostname via Trimmable interface
func printHostnameTrimmed(device Trimmable, trimlength int) {
	device.TrimHostname(trimlength)
	fmt.Printf("The hostname trimmed to %d characters is %s\n", trimlength, device.getHostname())
}

// Generics

type comparable interface {
	int | string | float64
}

func Min[T comparable](x, y T) T {
	if x < y {
		return x
	}
	return y
}

// Encoding

type NetworkInterface struct {
	Name  string `xml: "name" json: "name"`
	Speed int
}

type Device struct {
	Hostname   string
	Interfaces []NetworkInterface
}
