from Code.utils.load import load_text
from Code.utils.display import display_entities
from Code.entities import extract_entities
from Code.summarization import SumText

def test_med_ease():

    path = './data/test_med_text.csv'
    text = load_text(path)
    lines = text.split('\n')

    ans_summarize = [
        ' She does have asthma but does',
        ' Specifically denies chest pai',
        ' Extremities:  He has 1+ pitti'
    ]

    ans_add_definitions = [
        '"SUBJECTIVE:, ([\': of, relatin',
        '"PAST ([\': ago\', \'12 years pas',
        '"HISTORY ([\': tale, story\'])OF'
    ]

    ans_extract_entities = [
        [('complaint of allergies', 'DISEASE'), ('allergies', 'DISEASE'), ('asthma', 'DISEASE'), ('throat', 'DISEASE'), ('loratadine', 'CHEMICAL')],
        [('snoring', 'DISEASE'), ('pains', 'DISEASE'), ('knee pain', 'DISEASE'), ('pain', 'DISEASE'), ('ankle pain', 'DISEASE'), ('swelling', 'DISEASE'), ('gastroesophageal reflux diseasepast', 'DISEASE'), ('heart disease', 'DISEASE'), ('stroke', 'DISEASE'), ('diabetes', 'DISEASE'), ('obesity', 'DISEASE'), ('hypertension', 'DISEASE'), ('allergic', 'DISEASE'), ('chest pain', 'DISEASE'), ('coronary artery disease congestive heart failure arrhythmia', 'DISEASE'), ('atrial fibrillation', 'DISEASE'), ('cholesterol', 'CHEMICAL'), ('venous insufficiency thrombophlebitis asthma shortness of breath copd emphysema sleep apnea diabetes leg', 'DISEASE'), ('osteoarthritis rheumatoid arthritis hiatal hernia peptic ulcer disease gallstones infected gallbladder pancreatitis fatty liver hepatitis hemorrhoids', 'DISEASE'), ('bleeding polyps incontinence of stool urinary stress incontinence', 'DISEASE'), ('cancer', 'DISEASE'), ('cellulitis pseudotumor cerebri meningitis', 'DISEASE')],
        [('weight loss', 'DISEASE'), ('weight loss', 'DISEASE'), ('alcohol', 'CHEMICAL'), ('weight loss', 'DISEASE'), ('cholesterol', 'CHEMICAL'), ('asthma', 'DISEASE'), ('sleep apnea', 'DISEASE'), ('snoring', 'DISEASE'), ('diabetic', 'DISEASE'), ('pain knee pain', 'DISEASE'), ('pain', 'DISEASE'), ('ankle pain', 'DISEASE'), ('swelling', 'DISEASE'), ('alcohol', 'CHEMICAL'), ('heart disease', 'DISEASE'), ('diabetes', 'DISEASE'), ('hypertension', 'DISEASE'), ('diovan', 'CHEMICAL'), ('heart attacks', 'DISEASE'), ('gout', 'DISEASE'), ('chest pain heart attack coronary artery disease congestive heart failure arrhythmia atrial fibrillation', 'DISEASE'), ('pulmonary embolism', 'DISEASE'), ('venous insufficiency', 'DISEASE'), ('thrombophlebitis', 'DISEASE'), ('shortness of breath copd or emphysema  denies thyroid problems hip pain osteoarthritis rheumatoid arthritis gerd hiatal hernia peptic ulcer disease gallstones infected gallbladder pancreatitis fatty liver hepatitis rectal bleeding polyps incontinence of stool urinary stress incontinence', 'DISEASE'), ('cancer', 'DISEASE'), ('cellulitis pseudotumor cerebri meningitis', 'DISEASE'), ('wheezing', 'DISEASE'), ('pitting', 'DISEASE'), ('bleeding infection', 'DISEASE'), ('venous thrombosis pulmonary embolism', 'DISEASE'), ('bowel obstruction', 'DISEASE'), ('pylori', 'DISEASE')]
    ]

    result_entities = []

    for index, line in enumerate(lines):
        result = SumText(line)
        assert ans_summarize[index] == result.summarize()[:30]
        assert ans_add_definitions[index] == result.add_definitions()[:30]
        result_entities.append(extract_entities(line))

    assert ans_extract_entities == result_entities