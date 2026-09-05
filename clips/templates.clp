(deftemplate question
   (slot id)
   (slot area)
   (slot text)
   (multislot options)
)

(deftemplate answer
   (slot id)
   (slot score)
)

(deftemplate area-score
   (slot area)
   (slot score)
)

(deftemplate overall-score
   (slot value)
)

(deftemplate result
   (slot type)
   (slot message)
)