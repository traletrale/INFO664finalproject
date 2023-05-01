from matplotlib_venn import venn2, set_labels, set_edgecolor

# Input your data as a list of values
sets = {
    'MOMA': set(range(140848)),
    'Municipal': set(range(2642)),
    'Overlap': set(range(219))
}

# Create the Venn diagram
venn2(subsets=[len(sets['MOMA']) - len(sets['Overlap']), len(sets['Municipal']) - len(sets['Overlap']), len(sets['Overlap'])], set_edgecolor('white'))

# Remove labels
set_labels('', '', '')

# Display the Venn diagram
plt.show()
