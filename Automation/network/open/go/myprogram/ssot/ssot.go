package ssot

type SSOT struct {
	State string
}

func NewSSOT (state string) SSOT {
	return SSOT{State: state}
}