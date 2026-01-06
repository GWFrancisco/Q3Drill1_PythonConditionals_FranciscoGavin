from pyscript import display, document

# To compute the average of two quiz scores
def compute_average(event):
    # float - for potential decimal scores
    score1: float = float(document.getElementById("score1").value)
    score2: float = float(document.getElementById("score2").value)
    
    # float - computing the average
    avg: float = (score1 + score2) / 2
    
    # Condtionals used to computing the average
    if avg >= 75:
        result: str = f"Average: {avg:.2f} Passed"
    else:
        result: str = f"Average: {avg:.2f} Failed"
    
    # Display result
    display(result, target="output", append=False)