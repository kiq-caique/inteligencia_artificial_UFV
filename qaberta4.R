mult_imp_par_vetor <- function(a){
  i = 1
  par = 0
  impar = 0
  while(i <= length(a)){
    if(a[i] %% 2 == 0)
      par = par + a[i]
    else
      impar = impar + a[i]
    i = i+1
  }
  return(par*impar)
}

vetor1 = c(2,2,2,2,2)
vetor2 = c(2,1,1,1,1)
resposta = mult_imp_par_vetor(vetor1)
cat("\nResultado vetor 1: ", resposta)
resposta = mult_imp_par_vetor(vetor2)
cat("\nResultado vetor 2: ", resposta)