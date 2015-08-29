;;; https://projecteuler.net/problem=3
;;; The prime factors of 13195 are 5, 7, 13 and 29.
;;; What is the largest prime factor of the number 600851475143 ?

;; This isn't an ideal solution as each canidate has to be tested for being prime in a slightly better than brute force way

;; Ideally this would use some kind of sieve or at least track known primes for testing both would speed up runtime.

(defn prime? [value]
  "Returns true is value is prime and else otherwise. Test only up to the square root of value"
  (cond
   (= value 2) true ; special case 2
   (< value 2) false 
   :else (let [root (int (Math/sqrt value))] ; sqrt(value) is the max we need to prime for being prime
           (nil? (some #(zero? (mod value %)) (concat [2] (range 3 (inc root) 2)))))))

(println 
  (apply max ; find max of prime factors
         (filter 
           #(zero? (mod 600851475143 %)) ; test for being a factor
           (filter prime? 
                   (concat ; check 2, 3, 5, 7, ... (N+2) ... sqrt(600851475143)
                     [2] 
                     (range 3 (int (Math/sqrt 600851475143)) 2))))))
