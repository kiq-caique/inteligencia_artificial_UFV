par_impar <- function(a){
  if(a%%2 == 0)
    print("Número digitado é par")
  else
    print("Número digitado não é par")
}

par_impar(2)
par_impar(3)

print("Informe um número: ")
num <- scan(nmax=1)
par_impar(num)