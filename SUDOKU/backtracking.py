import sudoku_preader as reader

def BACKTRACKINGSEARCH(csp):# returns a solution, or failure
   return BACKTRACK({ }, csp)

def BACKTRACK(assignment,csp):
    if reader.is_complete(assignment[x], assignment[y], csp):
        return assignment
    var = reader.select_unassigned(csp)
    for value in order_domain_values(var):
        if reader.is_consistent(var, assignment, csp):
            csp[assignment[0]][assignment[1]] = value
            inferences = inferences(var, value)
            if inferences:
                csp[assignment[0]][assignment[1]] = value
                result = BACKTRACK(assignment, csp)
                if not result:
                    return result
        var = var.replace(value, "")
    return False

def inference(var, value):
    if var in value:
        return True

def order_domain_values(var):
    for v in var:
        return v

