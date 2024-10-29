from app import app, db  # Import your app and db from app.py
from models import Lawyer  # Import the Lawyer model


def seed_lawyers():
    lawyers = [
        Lawyer(lawyer_id=1, education='Lahore University of Management Sciences', specialization='Criminal Law', experience=5, hourly_rate=150.00, availability={"Mon": "9AM-5PM", "Wed": "10AM-4PM"}, location='Lahore', bio='Experienced criminal defense attorney.', user_id=1),
        Lawyer(lawyer_id=2, education='University of Karachi', specialization='Family Law', experience=7, hourly_rate=120.00, availability={"Tue": "9AM-5PM", "Thu": "9AM-3PM"}, location='Karachi', bio='Specializes in divorce and custody cases.', user_id=2),
        Lawyer(lawyer_id=3, education='Punjab University', specialization='Corporate Law', experience=10, hourly_rate=200.00, availability={"Mon": "9AM-5PM", "Wed": "9AM-5PM"}, location='Islamabad', bio='Expert in corporate regulations and compliance.', user_id=3),
        Lawyer(lawyer_id=4, education='University of the Punjab', specialization='Intellectual Property Law', experience=6, hourly_rate=175.00, availability={"Wed": "10AM-5PM", "Fri": "9AM-4PM"}, location='Lahore', bio='Specializes in intellectual property rights and patent laws.', user_id=4),
        Lawyer(lawyer_id=5, education='Bahria University', specialization='Tax Law', experience=8, hourly_rate=180.00, availability={"Mon": "9AM-4PM", "Thu": "11AM-6PM"}, location='Karachi', bio='Provides comprehensive tax advice and dispute resolution.', user_id=5),
        Lawyer(lawyer_id=6, education='National University of Sciences and Technology (NUST)', specialization='Civil Rights Law', experience=12, hourly_rate=220.00, availability={"Tue": "10AM-5PM", "Fri": "9AM-2PM"}, location='Rawalpindi', bio='Advocate for civil rights and public interest litigation.', user_id=6),
        Lawyer(lawyer_id=7, education='Kinnaird College for Women', specialization='Employment Law', experience=4, hourly_rate=140.00, availability={"Mon": "9AM-6PM", "Thu": "10AM-5PM"}, location='Lahore', bio='Assists clients with employment disputes and labor laws.', user_id=7),
        Lawyer(lawyer_id=8, education='Institute of Business Administration', specialization='Immigration Law', experience=9, hourly_rate=160.00, availability={"Tue": "9AM-4PM", "Wed": "10AM-3PM"}, location='Karachi', bio='Specializes in immigration and naturalization processes.', user_id=8),
        Lawyer(lawyer_id=9, education='University of Sindh', specialization='Criminal Law', experience=15, hourly_rate=230.00, availability={"Mon": "9AM-5PM", "Thu": "11AM-4PM"}, location='Hyderabad', bio='Highly experienced in criminal cases, including murder and theft.', user_id=9),
        Lawyer(lawyer_id=10, education='Quaid-i-Azam University', specialization='Environmental Law', experience=3, hourly_rate=120.00, availability={"Tue": "10AM-6PM", "Fri": "9AM-3PM"}, location='Islamabad', bio='Deals with environmental protection cases and disputes.', user_id=10),
        Lawyer(lawyer_id=11, education='Lahore School of Economics', specialization='Family Law', experience=6, hourly_rate=150.00, availability={"Mon": "9AM-5PM", "Wed": "10AM-6PM"}, location='Lahore', bio='Experienced in family law, including divorce and child custody.', user_id=11),
        Lawyer(lawyer_id=12, education='University of Balochistan', specialization='Human Rights Law', experience=5, hourly_rate=180.00, availability={"Tue": "10AM-6PM", "Thu": "10AM-4PM"}, location='Quetta', bio='Human rights lawyer with a focus on asylum cases.', user_id=12),
        Lawyer(lawyer_id=13, education='Shaheed Zulfikar Ali Bhutto Institute of Science and Technology', specialization='Corporate Law', experience=9, hourly_rate=220.00, availability={"Mon": "9AM-5PM", "Thu": "10AM-4PM"}, location='Karachi', bio='Provides legal counsel on corporate governance and mergers.', user_id=13),
        Lawyer(lawyer_id=14, education='University of Peshawar', specialization='Family Law', experience=8, hourly_rate=130.00, availability={"Wed": "9AM-5PM", "Thu": "10AM-6PM"}, location='Peshawar', bio='Specializes in family law with a focus on domestic violence.', user_id=14),
        Lawyer(lawyer_id=15, education='Forman Christian College', specialization='Intellectual Property Law', experience=7, hourly_rate=160.00, availability={"Tue": "9AM-6PM", "Fri": "9AM-3PM"}, location='Lahore', bio='Deals with intellectual property and trademark disputes.', user_id=15),
        Lawyer(lawyer_id=16, education='University of Karachi', specialization='Labor Law', experience=10, hourly_rate=180.00, availability={"Mon": "9AM-5PM", "Thu": "9AM-4PM"}, location='Karachi', bio='Expert in labor disputes and workers’ compensation.', user_id=16),
        Lawyer(lawyer_id=17, education='Iqra University', specialization='Criminal Law', experience=11, hourly_rate=210.00, availability={"Tue": "9AM-5PM", "Wed": "9AM-4PM"}, location='Islamabad', bio='Provides defense in serious criminal cases.', user_id=17),
        Lawyer(lawyer_id=18, education='University of the Punjab', specialization='Corporate Law', experience=6, hourly_rate=190.00, availability={"Mon": "9AM-5PM", "Thu": "9AM-4PM"}, location='Lahore', bio='Deals with corporate mergers and acquisitions.', user_id=18),
        Lawyer(lawyer_id=19, education='International Islamic University', specialization='Civil Law', experience=9, hourly_rate=160.00, availability={"Wed": "9AM-5PM", "Fri": "10AM-3PM"}, location='Rawalpindi', bio='Specializes in civil litigation and property disputes.', user_id=19),
        Lawyer(lawyer_id=20, education='University of Sindh', specialization='Immigration Law', experience=4, hourly_rate=140.00, availability={"Mon": "10AM-5PM", "Wed": "10AM-4PM"}, location='Hyderabad', bio='Focuses on immigration cases and asylum petitions.', user_id=20),
        Lawyer(lawyer_id=21, education='University of Peshawar', specialization='Employment Law', experience=8, hourly_rate=150.00, availability={"Tue": "9AM-5PM", "Thu": "9AM-3PM"}, location='Peshawar', bio='Employment and labor law specialist.', user_id=21),
        Lawyer(lawyer_id=22, education='Bahria University', specialization='Criminal Law', experience=14, hourly_rate=220.00, availability={"Mon": "9AM-6PM", "Fri": "9AM-4PM"}, location='Karachi', bio='Defense lawyer with over 14 years of experience in criminal cases.', user_id=22),
        Lawyer(lawyer_id=23, education='National University of Modern Languages', specialization='Intellectual Property Law', experience=6, hourly_rate=170.00, availability={"Tue": "9AM-5PM", "Thu": "10AM-4PM"}, location='Islamabad', bio='Handles intellectual property rights and licensing agreements.', user_id=23),
        Lawyer(lawyer_id=24, education='University of Balochistan', specialization='Environmental Law', experience=9, hourly_rate=200.00, availability={"Wed": "9AM-5PM", "Fri": "9AM-3PM"}, location='Quetta', bio='Deals with environmental litigation and disputes.', user_id=24),
        Lawyer(lawyer_id=25, education='Lahore University of Management Sciences', specialization='Family Law', experience=5, hourly_rate=140.00, availability={"Mon": "9AM-5PM", "Thu": "10AM-6PM"}, location='Lahore', bio='Specializes in divorce and child custody cases.', user_id=25),
        Lawyer(lawyer_id=26, education='Institute of Business Administration', specialization='Corporate Law', experience=7, hourly_rate=180.00, availability={"Mon": "9AM-5PM", "Wed": "10AM-4PM"}, location='Karachi', bio='Focuses on corporate transactions and regulatory compliance.', user_id=26),
        Lawyer(lawyer_id=27, education='Shaheed Zulfikar Ali Bhutto Institute of Science and Technology', specialization='Criminal Law', experience=6, hourly_rate=160.00, availability={"Tue": "9AM-6PM", "Thu": "9AM-4PM"}, location='Islamabad', bio='Provides legal defense in criminal proceedings.', user_id=27),
        Lawyer(lawyer_id=28, education='University of Peshawar', specialization='Tax Law', experience=8, hourly_rate=150.00, availability={"Wed": "10AM-6PM", "Fri": "9AM-3PM"}, location='Peshawar', bio='Specializes in tax law and regulatory compliance.', user_id=28),
        Lawyer(lawyer_id=29, education='International Islamic University', specialization='Civil Law', experience=12, hourly_rate=190.00, availability={"Mon": "9AM-5PM", "Thu": "9AM-4PM"}, location='Rawalpindi', bio='Handles civil litigation and property disputes.', user_id=29),
        Lawyer(lawyer_id=30, education='University of Karachi', specialization='Environmental Law', experience=5, hourly_rate=130.00, availability={"Tue": "9AM-5PM", "Fri": "9AM-3PM"}, location='Karachi', bio='Environmental lawyer focused on sustainability and protection.', user_id=30),
    ]

    db.session.bulk_save_objects(lawyers)
    db.session.commit()
    print("Seeded lawyers data.")
#  Main entry point
if __name__ == '__main__':
    with app.app_context():  # Use the app's application context
        seed_lawyers()