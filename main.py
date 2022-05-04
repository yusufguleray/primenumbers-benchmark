import time
import prime_finders		

if __name__ == "__main__":
	n = 10000
	start_t = time.time()
	prime_finders.prime_finder(n)
	elapsed_t = time.time() - start_t
	print("Elapsed time for finding",n,"number of prime number is:", elapsed_t, "seconds")