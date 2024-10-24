from app import app, db  # Import the app and db from your Flask app
from models import Review  # Import the Review model

def seed_reviews():
    reviews = [
        Review(review_id=1, user_id=31, lawyer_id=1, rating=5, comment='Ahmed provided excellent advice and helped me through a tough legal battle.'),
        Review(review_id=2, user_id=32, lawyer_id=1, rating=4, comment='Great experience with Ahmed, but a bit slow to respond at times.'),
        Review(review_id=3, user_id=33, lawyer_id=2, rating=5, comment='Fatima was very professional and helped resolve my custody case efficiently.'),
        Review(review_id=4, user_id=34, lawyer_id=2, rating=4, comment='Fatima handled my divorce well, but the process took longer than expected.'),
        Review(review_id=5, user_id=35, lawyer_id=3, rating=5, comment='Ali is a brilliant corporate lawyer. He helped my business a lot.'),
        Review(review_id=6, user_id=36, lawyer_id=3, rating=4, comment='Very good service, but I found his fees a bit high.'),
        Review(review_id=7, user_id=37, lawyer_id=4, rating=5, comment='Ayesha was amazing in handling my intellectual property case.'),
        Review(review_id=8, user_id=38, lawyer_id=4, rating=4, comment='She is knowledgeable, but communication could be better.'),
        Review(review_id=9, user_id=39, lawyer_id=5, rating=4, comment='Bilal helped with my tax case, though the resolution took time.'),
        Review(review_id=10, user_id=40, lawyer_id=5, rating=5, comment='Very satisfied with Bilal expertise and professional demeanor.'),
        Review(review_id=11, user_id=41, lawyer_id=6, rating=5, comment='Sara was fantastic in my civil rights case, very dedicated.'),
        Review(review_id=12, user_id=42, lawyer_id=6, rating=4, comment='She is highly experienced, but sometimes hard to reach.'),
        Review(review_id=13, user_id=43, lawyer_id=7, rating=5, comment='Usman provided great advice on my employment dispute.'),
        Review(review_id=14, user_id=44, lawyer_id=7, rating=4, comment='Good representation, but I felt the case could have been resolved faster.'),
        Review(review_id=15, user_id=45, lawyer_id=8, rating=5, comment='Zara was instrumental in my immigration process.'),
        Review(review_id=16, user_id=46, lawyer_id=8, rating=4, comment='Zara is very knowledgeable, but I felt communication was lacking.'),
        Review(review_id=17, user_id=47, lawyer_id=9, rating=5, comment='Hamza is an excellent criminal lawyer who handled my case very well.'),
        Review(review_id=18, user_id=48, lawyer_id=9, rating=4, comment='Great lawyer, but his fees were a bit on the higher side.'),
        Review(review_id=19, user_id=49, lawyer_id=10, rating=5, comment='Maryam’s guidance on environmental issues was spot-on.'),
        Review(review_id=20, user_id=50, lawyer_id=10, rating=4, comment='Good experience, but some delays in responses.'),
        Review(review_id=21, user_id=51, lawyer_id=11, rating=5, comment='Imran handled my family law case with great care and expertise.'),
        Review(review_id=22, user_id=52, lawyer_id=11, rating=4, comment='Imran was very helpful, though his availability could be better.'),
        Review(review_id=23, user_id=53, lawyer_id=12, rating=5, comment='Rabia was great with my human rights case, very passionate.'),
        Review(review_id=24, user_id=54, lawyer_id=12, rating=4, comment='Good lawyer, but the case took a little longer than expected.'),
        Review(review_id=25, user_id=55, lawyer_id=13, rating=5, comment='Fahad helped me greatly in a corporate legal matter.'),
        Review(review_id=26, user_id=56, lawyer_id=13, rating=4, comment='Very professional, but his office hours were a bit limited.'),
        Review(review_id=27, user_id=57, lawyer_id=14, rating=5, comment='Noor was fantastic in handling my family law case.'),
        Review(review_id=28, user_id=58, lawyer_id=14, rating=4, comment='Noor provided good service, though communication could be improved.'),
        Review(review_id=29, user_id=59, lawyer_id=15, rating=5, comment='Hassan is very skilled at intellectual property law.'),
        Review(review_id=30, user_id=60, lawyer_id=15, rating=4, comment='Hassan helped me with a patent issue, but the process was long.'),
        Review(review_id=31, user_id=31, lawyer_id=16, rating=5, comment='Mariam is highly knowledgeable in labor law.'),
        Review(review_id=32, user_id=32, lawyer_id=16, rating=4, comment='She helped me with a workplace dispute, though it took a bit longer.'),
        Review(review_id=33, user_id=33, lawyer_id=17, rating=5, comment='Shahzad is a great criminal lawyer.'),
        Review(review_id=34, user_id=34, lawyer_id=17, rating=4, comment='He defended me well, but the case took longer than expected.'),
        Review(review_id=35, user_id=35, lawyer_id=18, rating=5, comment='Nida was excellent in handling my corporate merger.'),
        Review(review_id=36, user_id=36, lawyer_id=18, rating=4, comment='She did a great job, but fees were a bit high.'),
        Review(review_id=37, user_id=37, lawyer_id=19, rating=5, comment='Waqas handled my civil litigation case with great skill.'),
        Review(review_id=38, user_id=38, lawyer_id=19, rating=4, comment='Good lawyer, but responses could be quicker.'),
        Review(review_id=39, user_id=39, lawyer_id=20, rating=5, comment='Sidra was a great help in my immigration case.'),
        Review(review_id=40, user_id=40, lawyer_id=20, rating=4, comment='Sidra is experienced, but I found communication a bit slow.'),
        Review(review_id=41, user_id=41, lawyer_id=21, rating=5, comment='Kashif was fantastic with my employment law case.'),
        Review(review_id=42, user_id=42, lawyer_id=21, rating=4, comment='He provided good representation, though the case took some time.'),
        Review(review_id=43, user_id=43, lawyer_id=22, rating=5, comment='Zainab is an excellent criminal lawyer.'),
        Review(review_id=44, user_id=44, lawyer_id=22, rating=4, comment='She defended me well, but her availability was sometimes limited.'),
        Review(review_id=45, user_id=45, lawyer_id=23, rating=5, comment='Tariq provided great advice on my intellectual property dispute.'),
        Review(review_id=46, user_id=46, lawyer_id=23, rating=4, comment='Tariq is knowledgeable, but the process took longer than expected.'),
        Review(review_id=47, user_id=47, lawyer_id=24, rating=5, comment='Aqsa was excellent in resolving my environmental case.'),
        Review(review_id=48, user_id=48, lawyer_id=24, rating=4, comment='Aqsa is good, but there were some delays in communication.'),
        Review(review_id=49, user_id=49, lawyer_id=25, rating=5, comment='Rizwan was very professional in handling my family law matter.'),
        Review(review_id=50, user_id=50, lawyer_id=25, rating=4, comment='Good service, but I wish communication had been faster.'),
        Review(review_id=51, user_id=51, lawyer_id=26, rating=5, comment='Shazia did an amazing job with my corporate legal case.'),
        Review(review_id=52, user_id=52, lawyer_id=26, rating=4, comment='Shazia is very competent, but her office hours were limited.'),
        Review(review_id=53, user_id=53, lawyer_id=27, rating=5, comment='Jawad defended me very well in my criminal case.'),
        Review(review_id=54, user_id=54, lawyer_id=27, rating=4, comment='Good lawyer, though the case took longer than anticipated.'),
        Review(review_id=55, user_id=55, lawyer_id=28, rating=5, comment='Mehwish helped me with tax planning. Very satisfied.'),
        Review(review_id=56, user_id=56, lawyer_id=28, rating=4, comment='Mehwish was great, though the process was a bit slow.'),
        Review(review_id=57, user_id=57, lawyer_id=29, rating=5, comment='Arslan resolved my civil litigation case excellently.'),
        Review(review_id=58, user_id=58, lawyer_id=29, rating=4, comment='Arslan provided good service, but communication could improve.'),
        Review(review_id=59, user_id=59, lawyer_id=30, rating=5, comment='Bushra handled my environmental case very well.'),
        Review(review_id=60, user_id=60, lawyer_id=30, rating=4, comment='Bushra is a knowledgeable lawyer, though responses were sometimes slow.')
    ]

    db.session.bulk_save_objects(reviews)
    db.session.commit()
    print("Seeded reviews data.")

if __name__ == '__main__':
    with app.app_context():  # Use the app's application context
        seed_reviews()
