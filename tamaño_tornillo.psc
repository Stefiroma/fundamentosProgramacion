Algoritmo tama�o_tornillo
	//NOMBRES:TATIANA RAVE, ESTEFANIA ROMA�A, DAVID OSORIO
	//FECHA:21/03/2023
	//PARCIAL EJERCICIO 3.
	//CREAR UN PROGRAMA QUE PIDA POR TECLADO EL TAMA�O DE UN TORNILLO Y MUESTRE EN PANTALLA EL TEXTO CORRESPONDIENTE AL TAMA�O
	
    Definir tamano_tornillo como real;
	Definir texto_tamano como cadena;
	
	Escribir "Introduce el tama�o correspondiente del tornillo: ";
	Leer tamano_tornillo;
  Si (1 <= tamano_tornillo) y (tamano_tornillo < 3) Entonces
		texto_tamano <- "peque�o";
	Fin Si
	Si (3 <= tamano_tornillo) y (tamano_tornillo < 5) Entonces
		texto_tamano <- "mediano";
	Fin Si
	Si (5 <= tamano_tornillo) y (tamano_tornillo < 6.5) Entonces
		texto_tamano <- "grande";
	Fin Si
	Si (6.5 <= tamano_tornillo) y (tamano_tornillo < 8.5) Entonces
		texto_tamano <- "muy grande";
	Fin Si
	Si (tamano_tornillo < 1) o (tamano_tornillo >= 8.5) Entonces
		texto_tamano <- "ERROR";
	Fin Si
	
    Escribir "El tama�o correspondiente del tornillo es ", texto_tamano;
	
FinAlgoritmo
