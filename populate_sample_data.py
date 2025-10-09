#!/usr/bin/env python
import os
import django
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calm_adventure_backend.settings')
django.setup()

from apps.blog.models import Category, BlogPost
from apps.services.models import Service
from apps.testimonials.models import Testimonial
from apps.team.models import TeamMember, JobOffer
from apps.core.models import SiteSettings
from django.contrib.auth import get_user_model

User = get_user_model()

def populate_data():
    # Get admin user
    admin_user = User.objects.get(username='admin')
    
    # Create site settings
    site_settings, created = SiteSettings.objects.get_or_create(
        id=1,
        defaults={
            'site_name': 'Lynkevo',
            'site_description': 'Votre partenaire de confiance pour un support client d\'exception et une croissance e-commerce durable.',
            'contact_email': 'hello@lynkevo.com',
            'contact_phone': '+261 34 99 781 85',
            'contact_address': 'Immeuble Nooro Tower, 4e étage\nAmbohitrarahaba, Antananarivo 103\nMadagascar',
            'meta_title': 'Lynkevo | Customer Service Specialists for E-commerce',
            'meta_description': 'Premier Customer Service Agency for E-commerce & Dropshippers. 24/7 multilingual support, expert teams, and scalable solutions.',
        }
    )
    
    # Create blog categories
    categories_data = [
        {'name': 'Support Client', 'name_en': 'Customer Support', 'color': '#FF0000'},
        {'name': 'E-commerce', 'name_en': 'E-commerce', 'color': '#844F76'},
        {'name': 'Innovation', 'name_en': 'Innovation', 'color': '#F39C12'},
        {'name': 'Design', 'name_en': 'Design', 'color': '#789AA1'},
        {'name': 'International', 'name_en': 'International', 'color': '#2ECC71'},
        {'name': 'Analytics', 'name_en': 'Analytics', 'color': '#9B59B6'},
    ]
    
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults=cat_data
        )
    
    # Create services
    services_data = [
        {
            'name': 'Support Client E-commerce',
            'name_en': 'E-commerce Customer Support',
            'slug': 'support-client-ecommerce',
            'short_description': 'Équipes dédiées 24/7 qui gèrent vos demandes clients, résolvent les problèmes et fidélisent votre clientèle.',
            'short_description_en': 'Dedicated 24/7 teams that handle customer inquiries, resolve issues, and build customer loyalty.',
            'description': '<p>Notre service de support client e-commerce est conçu spécifiquement pour les marques en ligne et les dropshippers. Nos équipes expertes gèrent tous vos canaux de communication client avec professionnalisme et efficacité.</p>',
            'description_en': '<p>Our e-commerce customer support service is specifically designed for online brands and dropshippers. Our expert teams manage all your customer communication channels with professionalism and efficiency.</p>',
            'icon': 'HeadphonesIcon',
            'starting_price': 299.00,
            'features': ['Support 24/7', 'Multilingue', 'Intégration CRM', 'Rapports détaillés'],
            'features_en': ['24/7 Support', 'Multilingual', 'CRM Integration', 'Detailed Reports'],
            'is_featured': True,
        },
        {
            'name': 'Développement Web & Apps',
            'name_en': 'Web & App Development',
            'slug': 'developpement-web-apps',
            'short_description': 'Applications web sur mesure et sites e-commerce performants.',
            'short_description_en': 'Custom web applications and high-performance e-commerce sites.',
            'description': '<p>Développement d\'applications web modernes et de sites e-commerce optimisés pour la conversion.</p>',
            'description_en': '<p>Development of modern web applications and e-commerce sites optimized for conversion.</p>',
            'icon': 'Code',
            'starting_price': 1999.00,
            'features': ['Technologies modernes', 'Responsive design', 'SEO optimisé', 'Maintenance incluse'],
            'features_en': ['Modern technologies', 'Responsive design', 'SEO optimized', 'Maintenance included'],
        },
    ]
    
    for service_data in services_data:
        service, created = Service.objects.get_or_create(
            slug=service_data['slug'],
            defaults=service_data
        )
    
    # Create testimonials
    testimonials_data = [
        {
            'name': 'Sarah Dubois',
            'position': 'Fondatrice',
            'company': 'Niche : Mode & Beauté',
            'content': 'Lynkevo a révolutionné notre service client. En 3 mois, notre temps de réponse a chuté de 80% et notre satisfaction client est passée de 70% à 98%.',
            'content_en': 'Lynkevo revolutionized our customer service. In 3 months, our response time dropped by 80% and our customer satisfaction went from 70% to 98%.',
            'rating': 5,
            'is_featured': True,
        },
        {
            'name': 'Michel Chen',
            'position': 'Directeur E-commerce',
            'company': 'Niche : High-Tech',
            'content': 'Pendant nos pics de vente, Lynkevo gère parfaitement l\'afflux de demandes. Leur réactivité et leur professionnalisme nous permettent de maintenir une expérience client premium.',
            'content_en': 'During our sales peaks, Lynkevo perfectly manages the influx of requests. Their responsiveness and professionalism allow us to maintain a premium customer experience.',
            'rating': 5,
            'is_featured': True,
        },
    ]
    
    for testimonial_data in testimonials_data:
        testimonial, created = Testimonial.objects.get_or_create(
            name=testimonial_data['name'],
            defaults=testimonial_data
        )
    
    # Create team members
    team_data = [
        {
            'name': 'Steve RAHARISON',
            'position': 'Fondateur & Développeur',
            'position_en': 'Founder & Developer',
            'bio': 'Passionné de technologie et d\'entrepreneuriat, Steve a fondé Lynkevo en 2011 avec la vision de révolutionner le support client e-commerce.',
            'bio_en': 'Passionate about technology and entrepreneurship, Steve founded Lynkevo in 2011 with the vision of revolutionizing e-commerce customer support.',
            'email': 'steve@lynkevo.com',
            'order': 1,
        },
        {
            'name': 'Lala RANDRIANASOLO',
            'position': 'Co-fondatrice & Customer Service Specialist',
            'position_en': 'Co-founder & Customer Service Specialist',
            'bio': 'Experte en relation client avec plus de 10 ans d\'expérience, Lala supervise la qualité de nos services et forme nos équipes.',
            'bio_en': 'Customer relations expert with over 10 years of experience, Lala oversees the quality of our services and trains our teams.',
            'email': 'lala@lynkevo.com',
            'order': 2,
        },
    ]
    
    for member_data in team_data:
        member, created = TeamMember.objects.get_or_create(
            name=member_data['name'],
            defaults=member_data
        )
    
    # Create job offers
    job_data = [
        {
            'title': 'Customer Support Specialist',
            'title_en': 'Customer Support Specialist',
            'department': 'Support Client',
            'employment_type': 'full_time',
            'experience_level': 'junior',
            'description': 'Nous recherchons un(e) spécialiste du support client passionné(e) pour rejoindre notre équipe dynamique.',
            'description_en': 'We are looking for a passionate customer support specialist to join our dynamic team.',
            'requirements': ['Excellente communication', 'Maîtrise du français et anglais', 'Expérience e-commerce appréciée'],
            'requirements_en': ['Excellent communication', 'Fluent in French and English', 'E-commerce experience appreciated'],
            'benefits': ['Télétravail possible', 'Formation continue', 'Équipe internationale'],
            'benefits_en': ['Remote work possible', 'Continuous training', 'International team'],
            'location': 'Antananarivo, Madagascar',
            'remote_possible': True,
            'salary_min': 800.00,
            'salary_max': 1200.00,
        },
    ]
    
    for job in job_data:
        job_offer, created = JobOffer.objects.get_or_create(
            title=job['title'],
            defaults=job
        )
    
    print("Sample data populated successfully!")

if __name__ == '__main__':
    populate_data()