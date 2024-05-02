soma_mult_sub <- function(a, b){#3, 2
  soma = a+b
  mult = a*b
  sub1 = a-b #1
  sub2 = b-a #-1
  
  if (soma %% 2 == 0)
    print(paste("Essa é uma soma par:", soma))
  if (mult %% 3 == 0)
    print(paste("Multiplicação resultou em número múltiplo de 3:", mult))
  if (sub1 > sub2)
    print(paste("Maior das subtrações é sub1:", sub1))
  else
    print(paste("Maior das subtrações é sub2:", sub2))
}

cat("\nResultado teste 1:\n")
soma_mult_sub(3,3)

cat("\nResultado teste 2:\n")
soma_mult_sub(3,2)
