package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		contenedor, _ := os.Hostname()
		fmt.Fprintf(w, "¡Hola desde Go! Te responde el contenedor %s\n", contenedor)
	})

	log.Println("Escuchando en el puerto 8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
