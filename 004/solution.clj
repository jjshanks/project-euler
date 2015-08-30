;;; https://projecteuler.net/problem=4
;;; A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
;;; Find the largest palindrome made from the product of two 3-digit numbers.

(defn rev-num 
  "Reverse a num. For example 123 would become 321"
  [value]
  (loop
    [r (rem value 10) q (quot value 10) total 0]
    (let [new-total (+ (* total 10) r)]
      (if
        (> q 0)
        (recur (rem q 10) (quot q 10) new-total)
        new-total))))

(println
  (apply max
         (filter #(= (rev-num %) %) ; palidrome test
                 (for
                   [left (range 100 1000)
                    right (range 100 1000)]
                    (* left right)))))
