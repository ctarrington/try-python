import seaborn as sns

def augment_tips():
    tips = sns.load_dataset('tips')

    tips['per_person_bill'] = tips['total_bill'] / tips['size']
    tips['tip_percent'] = tips['tip'] / tips['total_bill']
    tips = tips.query('per_person_bill > 3 & tip_percent < 0.5 & size > 1')
    return tips



