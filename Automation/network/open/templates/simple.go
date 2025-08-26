package main

import (
	"os"
	"strconv"
	"strings"
	"text/template"
)

type Switch struct {
	Hostname       string
	InterfaceCount uint
}

type Sw struct {
	Hostname   string
	Interfaces []string
}

type Switches struct {
	Hostname       string
	InterfaceCount uint
	Enabled        bool
}

func main() {
	// We can create an inline template using the Parse() method of the
	// template.Template type
	//
	// Note that simpleTemplate is just an arbitrary name chosen for
	// this example.
	tmpl, err := template.New("simple").Parse(`{{ "foobar\n" |
	print }}`)
	if err != nil {
		panic(err)
	}
	// We can render the template with Execute, passing in os.Stdout
	// as the first parameter, so we can see the results in our
	// terminal
	err = tmpl.Execute(os.Stdout, nil)
	if err != nil {
		panic(err)
	}

	sw01 := Switch{"sw01", 48}

	templ, err := template.New("switch").Parse("Device {{.Hostname}} has {{.InterfaceCount}} interfaces \n")
	if err != nil {
		panic(nil)
	}
	err = templ.Execute(os.Stdout, sw01)
	if err != nil {
		panic(nil)
	}

	switches := []Switch{
		{"sw01", 48},
		{"sw02", 49},
		{"sw03", 50},
	}
	tmplStr := `
	{{range $i, $switch := .}}
	Device {{$switch.Hostname}} has {{$switch.InterfaceCount}} interfaces {{end}}`

	temp, err := template.New("switch").Parse(tmplStr)
	if err != nil {
		panic(nil)
	}
	err = temp.Execute(os.Stdout, switches)
	if err != nil {
		panic(nil)
	}

	my_switches := []Switches{
		{"sw01", 51, true},
		{"sw02", 52, false},
		{"sw03", 53, true},
		{"sw04", 54, false},
		{"sw05", 55, true},
	}

	tempStr := `
	{{range $i, $switch := .}}
	{{if $switch.Enabled}}
	Device {{$switch.Hostname}} has {{$switch.InterfaceCount}} interfaces
	{{end}} 
	{{end}}`

	tmp, err := template.New("simple").Parse(tempStr)
	if err != nil {
		panic(err)
	}
	err = tmp.Execute(os.Stdout, my_switches)
	if err != nil {
		panic(err)
	}

	your_switches := map[string]int{
		"sw01": 48,
		"sw02": 24,
		"sw03": 48,
	}
	// Since we're now iterating over a map, the two created variables
	// after the
	// range keyword represent each key/value pair
	tmplStrng := `
	{{range $hostname, $ifCount := .}}
	Device {{$hostname}} has {{$ifCount}} interfaces
	{{end}}
	`
	tmplt, err := template.New("simple").Parse(tmplStrng)
	if err != nil {
		panic(err)
	}
	err = tmplt.Execute(os.Stdout, your_switches)
	if err != nil {
		panic(err)
	}

	our_switch := Sw{
		"sw01", []string{
			"g0/1",
			"g0/2"}}

	tmpltStr := `
	Device {{.Hostname}} has {{ .Interfaces | len }} interfaces\n`

	tmpt, err := template.New("simple").Parse(tmpltStr)

	if err != nil {
		panic(err)
	}
	err = tmpt.Execute(os.Stdout, our_switch)
	if err != nil {
		panic(err)
	}

	fmap := template.FuncMap{"ifparse": IfParse}
	swc01 := Sw{"sw01", []string{
		"ge-0/0/1",
		"ge-0/0/2",
		"ge-0/0/3",
		"ge-0/0/4"}}

	tp := `{{range $i, $interface := .Interfaces}}
	{{with $loc := $interface | ifparse}}
	Interface {{$interface}} port {{$loc.Port}}
	{{end}}
	{{end}}`

	tmplte, err :=
		template.New("switchTemplate").Funcs(fmap).Parse(tp)
	if err != nil {
		panic(err)
	}
	err = tmplte.Execute(os.Stdout, swc01)
	if err != nil {
		panic(err)
	}

}

type Interface struct {
	Speed int
	FPC   int
	PIC   int
	Port  int
}

func IfParse(ifaceStr string) Interface {
	iface := Interface{}
	ifSplit := strings.Split(ifaceStr, "-")
	speeds := map[string]int{
		"ge": 1,
		"xe": 10,
		"et": 40,
	}
	iface.Speed = speeds[ifSplit[0]]
	locSplit := strings.Split(ifSplit[1], "/")
	fpc, _ := strconv.Atoi(locSplit[0])
	iface.FPC = fpc
	pic, _ := strconv.Atoi(locSplit[1])
	iface.PIC = pic
	port, _ := strconv.Atoi(locSplit[2])
	iface.Port = port
	return iface
}
