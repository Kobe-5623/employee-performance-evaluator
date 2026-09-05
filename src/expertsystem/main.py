import customtkinter as ctk
import clips

def newOption(app, text, value, selected_option):
  option = ctk.CTkFrame( app, width=400, height=50, fg_color="#2E2E2E" )
  option.pack_propagate( False )
  option.pack( padx=50, pady=10 )

  radio = ctk.CTkRadioButton( 
    option, radiobutton_width=16, radiobutton_height=16, 
    border_width_checked="5", border_width_unchecked=2,
    text=text,
    value=value,
    variable=selected_option
  )
  radio.pack( side="left", padx=15 )

  return option

def main():

  # CLIPS ----- BAKA ILIPAT KO SA SEPARATE NA FILE, DEPENDE PA

  env = clips.Environment()

  env.load("clips/config.clp")
  env.load("clips/questions.clp")

  env.reset()

  template = env.find_template("configuration")
  fact = next(template.facts())
  student_count = fact["student-count"]

  template = env.find_template("question")
  questions = list(template.facts())

  question = questions[0]






  # UI -------

  app = ctk.CTk()
  app.title("Teacher Performance Evaluator")
  app.geometry("500x600")


  displayed_question = ctk.CTkLabel(app, text=question["text"])
  displayed_question.pack(padx=50, pady=10)

  selected_option = ctk.StringVar(value="")

  for index, option in enumerate(question["options"]):
    newOption(app, option, index + 1, selected_option)

  app.mainloop()

if __name__ == "__main__":
  main()