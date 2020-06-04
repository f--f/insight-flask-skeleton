import matplotlib.pyplot as plt
# import sklearn, etc.


def run_model(model_input):
    """Return output of model."""
    # ----
    # insert your business logic here
    # ----
    output = f"<model output based on the input: {model_input}>"
    return output


def create_plot(model_input):
    """Return filename of a plot saved to static/ folder."""
    fname = model_input + ".png"
    f, ax = plt.subplots()
    ax.plot([0,1,2], [4,5,6], "ro")
    ax.set_title(model_input)
    f.savefig("static/" + fname) 
    return fname