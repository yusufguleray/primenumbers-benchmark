def prime_finder(n_primes):
	primes=[]
	i=2
	while len(primes)<n_primes:
		is_prime = True
		for prime in primes:
			if i%prime == 0:
				is_prime = False
				break
		if is_prime: primes.append(i)
		i+=1
	return primes