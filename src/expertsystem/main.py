import customtkinter as ctk
import clips


def load_clips():
    env = clips.Environment()
    env.load("clips/templates.clp")
    env.load("clips/questions.clp")
    env.load("clips/rules.clp")
    env.reset()
    return env


def main():
    env = load_clips()
    questions = sorted(
        list(env.find_template("question").facts()),
        key=lambda q: int(q["id"])
    )

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Employee Performance Evaluation")
    app.geometry("650x570")
    app.resizable(False, False)

    ctk.CTkLabel(
        app,
        text="Employee Performance Evaluation",
        font=("Arial", 22, "bold")
    ).pack(pady=(10, 2))

    ctk.CTkLabel(
        app,
        text="Rate the employee based on their performance.",
        font=("Arial", 13)
    ).pack(pady=(0, 5))

    form = ctk.CTkScrollableFrame(
        app,
        width=570,
        height=390
    )
    form.pack(padx=20, pady=3)

    answers = []

    areas = [
        "Work Performance",
        "Communication & Teamwork",
        "Compliance & Accountability",
        "Problem Solving & Adaptability",
        "Quality & Professionalism"
    ]

    for area in areas:
        ctk.CTkLabel(
            form,
            text=area,
            font=("Arial", 16, "bold")
        ).pack(anchor="w", pady=(10, 5))

        for question in questions:
            if str(question["area"]) != area:
                continue

            ctk.CTkLabel(
                form,
                text=f'{question["id"]}. {question["text"]}',
                font=("Arial", 13, "bold"),
                wraplength=540,
                justify="left"
            ).pack(anchor="w", pady=(4, 3))

            selected = ctk.IntVar(value=0)
            answers.append((question, selected))

            for score in range(1, 6):
                ctk.CTkRadioButton(
                    form,
                    text=question["options"][score - 1],
                    variable=selected,
                    value=score,
                    font=("Arial", 12)
                ).pack(anchor="w", padx=15, pady=1)

    error = ctk.CTkLabel(
        app,
        text="",
        text_color="red",
        font=("Arial", 11)
    )
    error.pack(pady=1)

    def submit():
        for question, selected in answers:
            if selected.get() == 0:
                error.configure(
                    text=f'Please answer question {question["id"]}.'
                )
                return

        for question, selected in answers:
            env.assert_string(
                f'(answer (id {question["id"]}) (score {selected.get()}))'
            )

        env.run()

        result = list(env.find_template("result").facts())[0]
        overall = list(env.find_template("overall-score").facts())[0]
        area_scores = list(env.find_template("area-score").facts())

        show_result(result, overall, area_scores)

    ctk.CTkButton(
        app,
        text="Submit Evaluation",
        width=190,
        height=36,
        command=submit
    ).pack(pady=(2, 7))

    def show_result(result, overall, area_scores):
        for widget in app.winfo_children():
            widget.destroy()

        ctk.CTkLabel(
            app,
            text="Evaluation Result",
            font=("Arial", 24, "bold")
        ).pack(pady=(25, 10))

        ctk.CTkLabel(
            app,
            text=str(result["type"]),
            font=("Arial", 21, "bold")
        ).pack(pady=4)

        ctk.CTkLabel(
            app,
            text=f'Overall Score: {float(overall["value"]):.2f} / 5.00',
            font=("Arial", 16)
        ).pack(pady=4)

        ctk.CTkLabel(
            app,
            text=str(result["message"]),
            font=("Arial", 12),
            wraplength=500
        ).pack(pady=7)

        ctk.CTkLabel(
            app,
            text="Area Scores",
            font=("Arial", 17, "bold")
        ).pack(pady=(10, 7))

        for area_name in areas:
            for area in area_scores:
                if str(area["area"]) == area_name:
                    ctk.CTkLabel(
                        app,
                        text=f'{area_name}: {float(area["score"]):.2f} / 5.00',
                        font=("Arial", 12)
                    ).pack(pady=2)

        ctk.CTkButton(
            app,
            text="Exit",
            width=130,
            command=app.destroy
        ).pack(pady=15)

    app.mainloop()


if __name__ == "__main__":
    main()