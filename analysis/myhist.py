import seaborn as sns
import matplotlib.pyplot as plt

def df_hist_grid(df, rows, columns, figsize, border_vis=[False, False, False, False], label_rotation = 90, fontsize=10):
    """input:
           df: barplot data 
           border_vis: list of boolean values signaling presence of spine, 
                       clockwise starting at top spine
           label_rotation: degree of x label rotation 
       output:
           plotted grid of histograms 
    """
    i, j = 0, 0
    f, axes = plt.subplots(rows, columns, figsize =figsize)
    plt.subplots_adjust(hspace = .45)

    for col in df.columns:
        bar_data = df[col].value_counts()
        sns.barplot(bar_data.index, bar_data.values, ax = axes[i,j], )
        axes[i, j].set_title(col)
        axes[i, j].spines['top'].set_visible(border_vis[0])
        axes[i, j].spines['right'].set_visible(border_vis[1])
        axes[i, j].spines['bottom'].set_visible(border_vis[2])
        axes[i, j].spines['left'].set_visible(border_vis[3])
        axes[i, j].tick_params(axis='x', rotation=label_rotation)

        j += 1 
        if j ==columns:
            i += 1
            j = 0

            
if __name__=='__main__':
    pass