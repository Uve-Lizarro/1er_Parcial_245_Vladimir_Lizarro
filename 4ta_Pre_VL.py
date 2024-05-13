from kanren import Relation, facts, run, var, conde
#Vladimir Ariel Lizarro Velasquez
padres=Relation()
abuelos=Relation()
tios=Relation()
hermanos=Relation()
primos=Relation()

facts(padres, ("W", "V"), ("P", "V"), ("W", "A"), ("P", "A"))
facts(abuelos, ("A1", "V"), ("A2", "V"), ("A1", "A"), ("A2", "A"))
facts(tios, ("T1", "V"), ("T2", "V"), ("T1", "A"), ("T2", "A"))
facts(hermanos, ("A", "V"), ("V", "A"))
facts(primos, ("P1", "V"), ("P2", "V"), ("P1", "A"), ("P2", "A"))

def relPadres(x, z):
  return conde((padres(x, z),))

def relAbuelos(x, z):
  return conde((abuelos(x, z),))

def relTios(x, z):
  return conde((tios(x, z),))

def relHermanos(x, z):
  return conde((hermanos(x, z),))

def relPrimos(x, z):
  return conde((primos(x, z),))

if __name__ == '__main__':
  x=var()
  n=input("Persona: ").capitalize()

  resultado = run(2, x, relPadres(x, n))
  print(f"Padres de {n}: {resultado}")

  resultado = run(2, x, relHermanos(x, n))
  print(f"Hermanos de {n}: {resultado}")

  resultado = run(2, x, relAbuelos(x, n))
  print(f"Abuelos de {n}: {resultado}")

  resultado = run(2, x, relTios(x, n))
  print(f"Tíos de {n}: {resultado}")

  resultado = run(2, x, relPrimos(x, n))
  print(f"Primos de {n}: {resultado}")