(define make-fridge

  (lambda (amount-food)

    (define add-food 
      (lambda (amount)
        (if (> amount 0)
          (begin
            (set! amount-food (+ amount-food amount))
            amount-food)
          'ERROR
          )))

    (define remove-food
      (lambda (amount)
        (if (< amount 0)
          (begin
            (set! amount-food (- amount-food amount))
            amount-food)
          'ERROR)))

    (define delegator
      (lambda (message)
        (if (equal? message 'add)
          add-food
          (if (equal? message 'remove)
            remove-food
            'ERROR))))

    delegator))


(define fridge (make-fridge 42))
((fridge 'add) 3)
