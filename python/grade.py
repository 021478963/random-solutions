def grade(hw, assignment, midterm, midtermOption, final, finalOption):
    return (0.1 * hw + 0.4 * assignment + 0.1 * midterm + 0.1 * midtermOption * midterm + 0.2 * final + 0.1 * final * finalOption) / (0.8 + 0.1 * midtermOption + 0.1 * finalOption)

print(grade(100, 0, 0, 0, 0, 0,))