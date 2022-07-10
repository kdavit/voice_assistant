# ვაიმპორტებთ შესაბამის პაკეტებს
import pyjokes
import listenAndSpeak
import re

# default ენა და default კატეგორია თუ არ მიუთითებ ეს ენა და კატეგორია აირჩევა
language = 'en'
category = 'neutral'


# comands =["say joke","tell me joke","tell us joke","make joke","make us happy"]
# language =["en","de","es","it","gl","eu"]
# category =['neutral', 'chuck', 'all']

# change language  არგუმენტად გადავცემთ ენას რა ენაც გვინდა სრული სიტყვა მაგალითად ინგლური
# და შესაბამისად "en" დააბრუნებს
def ChangeL(argument):
    swicher = {
        "english": "en",
        "german": "de",
        "spanish": "es",
        "italian": "it",
        "galician": "gl",
        "basque": "eu"
    }
    return swicher[argument]


def telljoke(text):
    # change category if it is in text
    # ეძებს თუ არის გადმოცემულ ტექტსში რაიმე კატეგორია რეჯექსების გამოყენებით თუ არა დეფაულტად რაც უწერია იმ კატეგორიას იყენებს
    searchCategory = re.search(".*category.*(neutral|chuck|all)", text)

    # თუ კატეგორია მოიძებნა შესაბამისად seacrchCategoty  null არ იქენბა
    # category უტოლებ searchCategory.group(1) ეს ნიშნავს რომ (neutral|chuck|all) აქედან რომელიც დაემთხვევა
    # გადმოცემული ტექსტიდან იმას არიჩევს
    if searchCategory:
        category = searchCategory.group(1)
    else:
        category = "neutral"

    # change language if it is in text
    # აქაც ვიყენბთ რეჯექსებს რომ ვიპოვოთ ტექსში შესაბამისი ენა (რეჯექსი ტექსტიდან დაიჭერს შესაბამის სიტყვას)
    # შემდეგ გამოიძახებს ფუნქციას რომელიც დააბრუნებს შესაბამის კატეგორიას
    changeLanguage = re.search("(language|in).*(english|german|spanish|italian|galician|basque)", text)
    if changeLanguage:
        language = ChangeL(changeLanguage.group(2))
    else:
        language = "en"

    # აქ გამოვიყენებთ pyjokes.get_joke რომელსაც მიუთითებთ ენას და კატეგორიას
    joke = pyjokes.get_joke(language=language, category=category)
    print("Text you sad : " + text)
    print("joke : " + joke)
    # ხუმრობას ტექტსტის სახით ვაბრუნებთ
    return joke
