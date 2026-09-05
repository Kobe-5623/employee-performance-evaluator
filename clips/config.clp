(deftemplate configuration
    (slot student-count)
)

(deffacts config
    (configuration
        (student-count 25)
    )
)