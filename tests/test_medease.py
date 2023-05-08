from Code.utils.load import load_text
from Code.utils.display import display_entities
from Code.entities import extract_entities
from Code.summarization import SumText
import os


def test_med_ease():

    ans_summarize = [
        ' Extremities:  He has 1+ pitti',
        ' Specifically denies chest pai',
        ' She does have asthma but does'
    ]

    ans_add_definitions = [
        '"HISTORY ([\': tale, story\'])OF',        
        '"PAST ([\': ago\', \'12 years pas',
        '"SUBJECTIVE:, ([\': of, relatin'
    ]

    ans_extract_entities = [
        [('weight loss', 'DISEASE'), ('weight loss', 'DISEASE'), ('alcohol', 'CHEMICAL'), ('weight loss', 'DISEASE'), ('cholesterol', 'CHEMICAL'), ('asthma', 'DISEASE'), ('sleep apnea', 'DISEASE'), ('snoring', 'DISEASE'), ('diabetic', 'DISEASE'), ('pain knee pain', 'DISEASE'), ('pain', 'DISEASE'), ('ankle pain', 'DISEASE'), ('swelling', 'DISEASE'), ('alcohol', 'CHEMICAL'), ('heart disease', 'DISEASE'), ('diabetes', 'DISEASE'), ('hypertension', 'DISEASE'), ('diovan', 'CHEMICAL'), ('heart attacks', 'DISEASE'), ('gout', 'DISEASE'), ('chest pain heart attack coronary artery disease congestive heart failure arrhythmia atrial fibrillation', 'DISEASE'), ('pulmonary embolism', 'DISEASE'), ('venous insufficiency', 'DISEASE'), ('thrombophlebitis', 'DISEASE'), ('shortness of breath copd or emphysema  denies thyroid problems hip pain osteoarthritis rheumatoid arthritis gerd hiatal hernia peptic ulcer disease gallstones infected gallbladder pancreatitis fatty liver hepatitis rectal bleeding polyps incontinence of stool urinary stress incontinence', 'DISEASE'), ('cancer', 'DISEASE'), ('cellulitis pseudotumor cerebri meningitis', 'DISEASE'), ('wheezing', 'DISEASE'), ('pitting', 'DISEASE'), ('bleeding infection', 'DISEASE'), ('venous thrombosis pulmonary embolism', 'DISEASE'), ('bowel obstruction', 'DISEASE'), ('pylori', 'DISEASE')],
        [('snoring', 'DISEASE'), ('pains', 'DISEASE'), ('knee pain', 'DISEASE'), ('pain', 'DISEASE'), ('ankle pain', 'DISEASE'), ('swelling', 'DISEASE'), ('gastroesophageal reflux diseasepast', 'DISEASE'), ('heart disease', 'DISEASE'), ('stroke', 'DISEASE'), ('diabetes', 'DISEASE'), ('obesity', 'DISEASE'), ('hypertension', 'DISEASE'), ('allergic', 'DISEASE'), ('chest pain', 'DISEASE'), ('coronary artery disease congestive heart failure arrhythmia', 'DISEASE'), ('atrial fibrillation', 'DISEASE'), ('cholesterol', 'CHEMICAL'), ('venous insufficiency thrombophlebitis asthma shortness of breath copd emphysema sleep apnea diabetes leg', 'DISEASE'), ('osteoarthritis rheumatoid arthritis hiatal hernia peptic ulcer disease gallstones infected gallbladder pancreatitis fatty liver hepatitis hemorrhoids', 'DISEASE'), ('bleeding polyps incontinence of stool urinary stress incontinence', 'DISEASE'), ('cancer', 'DISEASE'), ('cellulitis pseudotumor cerebri meningitis', 'DISEASE')],
        [('complaint of allergies', 'DISEASE'), ('allergies', 'DISEASE'), ('asthma', 'DISEASE'), ('throat', 'DISEASE'), ('loratadine', 'CHEMICAL')]
    ]

    folder_path = './data'
    files = os.listdir(folder_path)

    for index, file in enumerate(files):

        file_path = os.path.join(folder_path, file)
        text = load_text(file_path)

        result = SumText(text)

        assert ans_summarize[index] == result.summarize()[:30]
        assert ans_add_definitions[index] == result.add_definitions()[:30]
        assert ans_extract_entities[index] == extract_entities(text)