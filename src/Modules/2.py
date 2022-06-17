 br1 = np.arange(len(food))
                br2 = [x + barWidth for x in br1]
                br3 = [x + barWidth for x in br2]
                br4 = [x + barWidth for x in br3]
                br5 = [x + barWidth for x in br4]

                plt.bar(br1, sports, color='red', width=barWidth,
                        edgecolor='grey', label='Sports and travel')

                plt.bar(br2, food, color='green', width=barWidth,
                        edgecolor='grey', label='food and beverages')

                plt.bar(br3, fashion, color='blue', width=barWidth,
                        edgecolor='grey', label='fashion accessories')

                plt.bar(br4, health, color='cyan', width=barWidth,
                        edgecolor='grey', label='Health')

                plt.bar(br5, electronics, color='black', width=barWidth,
                        edgecolor='grey', label='electronics')
                
                # Adding Xticks
                plt.xlabel('Gender')
                plt.ylabel('Number of people')
                plt.xticks([r + barWidth for r in range(len(food))],
                           [f'male-{totalMale}', f'female-{totalFemale}'])
                plt.legend()
                plt.show()
                break