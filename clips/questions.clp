(deftemplate question
  (slot id)
  (slot text)
  (multislot options)
)

(deffacts questionnaire

  (question (id 1)
    (text "How often does the student participate in class?")
    (options
      "Never"
      "Rarely"
      "Sometimes"
      "Often"
      "Very Often"
      "Always"
    )
  )

  (question (id 2)
    (text "How often does the student complete assignments on time?")
    (options
      "Never"
      "Rarely"
      "Sometimes"
      "Often"
      "Very Often"
      "Always"
    )
  )

  (question (id 3)
    (text "How well does the student work with others?")
    (options
      "Never"
      "Rarely"
      "Sometimes"
      "Often"
      "Very Often"
      "Always"
    )
  )
)