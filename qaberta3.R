soma_loop = function(a,b){ 
  soma = a+b 
  while(soma>0){ 
    if(soma%%2 == 0)
      a = a-1 
    else
      b = b-3 
    soma = a+b 
    cat("\nSoma a+b= ",soma)
  }
}

cat("\nResultado teste 1:")
soma_loop(3, 3)

cat("\nResultado teste 2:")
soma_loop(3, 2)
