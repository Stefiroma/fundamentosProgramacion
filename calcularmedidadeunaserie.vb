Module CALCULARMEDIDADEUNASERIE

	Sub Main()
		Dim media As Double
		Dim n As Double
		Dim suma As Double
		Dim total As Integer
		Dim x As Integer
		Console.WriteLine("Ingresa el total de numeros")
		total = Integer.Parse(Console.ReadLine())
		x = 0
		suma = 0
		While x<=total
			Console.WriteLine("Ingresa el numero ",x)
			n = Double.Parse(Console.ReadLine())
			suma = suma+n
			x = x+1
		End While
		media = suma/total
		Console.WriteLine("La media aritmetica es: ",media)
	End Sub

End Module
