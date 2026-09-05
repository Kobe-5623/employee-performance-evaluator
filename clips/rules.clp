(defrule calculate-work-performance
   (answer (id 1) (score ?s1))
   (answer (id 2) (score ?s2))
   =>
   (assert
      (area-score
         (area "Work Performance")
         (score (/ (+ ?s1 ?s2) 2))
      )
   )
)

(defrule calculate-communication-teamwork
   (answer (id 3) (score ?s1))
   (answer (id 4) (score ?s2))
   =>
   (assert
      (area-score
         (area "Communication & Teamwork")
         (score (/ (+ ?s1 ?s2) 2))
      )
   )
)

(defrule calculate-compliance-accountability
   (answer (id 5) (score ?s1))
   (answer (id 6) (score ?s2))
   =>
   (assert
      (area-score
         (area "Compliance & Accountability")
         (score (/ (+ ?s1 ?s2) 2))
      )
   )
)

(defrule calculate-problem-solving-adaptability
   (answer (id 7) (score ?s1))
   (answer (id 8) (score ?s2))
   =>
   (assert
      (area-score
         (area "Problem Solving & Adaptability")
         (score (/ (+ ?s1 ?s2) 2))
      )
   )
)

(defrule calculate-quality-professionalism
   (answer (id 9) (score ?s1))
   (answer (id 10) (score ?s2))
   =>
   (assert
      (area-score
         (area "Quality & Professionalism")
         (score (/ (+ ?s1 ?s2) 2))
      )
   )
)

(defrule calculate-overall-score
   (area-score (area "Work Performance") (score ?s1))
   (area-score (area "Communication & Teamwork") (score ?s2))
   (area-score (area "Compliance & Accountability") (score ?s3))
   (area-score (area "Problem Solving & Adaptability") (score ?s4))
   (area-score (area "Quality & Professionalism") (score ?s5))
   =>
   (bind ?score
      (+
         (* ?s1 0.30)
         (* ?s2 0.20)
         (* ?s3 0.15)
         (* ?s4 0.15)
         (* ?s5 0.20)
      )
   )

   (assert
      (overall-score
         (value ?score)
      )
   )
)

(defrule determine-result
   (overall-score (value ?score))
   =>
   (if (>= ?score 4.50)
      then
      (assert
         (result
            (type "Excellent")
            (message "Employee demonstrates excellent overall performance.")
         )
      )
      else
      (if (>= ?score 3.50)
         then
         (assert
            (result
               (type "Very Satisfactory")
               (message "Employee demonstrates very satisfactory overall performance.")
            )
         )
         else
         (if (>= ?score 2.50)
            then
            (assert
               (result
                  (type "Satisfactory")
                  (message "Employee demonstrates satisfactory overall performance.")
               )
            )
            else
            (assert
               (result
                  (type "Needs Improvement")
                  (message "Employee needs improvement in overall performance.")
               )
            )
         )
      )
   )
)