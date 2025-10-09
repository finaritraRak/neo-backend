#!/usr/bin/env python
import os
import django
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calm_adventure_backend.settings')
django.setup()

from apps.blog.models import Category, BlogPost
from django.contrib.auth import get_user_model

User = get_user_model()

def populate_blog_data():
    # Get admin user
    admin_user = User.objects.get(username='admin')
    
    # Create categories
    categories_data = [
        {
            'name': 'Support Client',
            'name_en': 'Customer Support',
            'slug': 'support-client',
            'description': 'Articles sur le support client et la relation client',
            'color': '#FF0000'
        },
        {
            'name': 'E-commerce',
            'name_en': 'E-commerce',
            'slug': 'ecommerce',
            'description': 'Conseils et stratégies e-commerce',
            'color': '#844F76'
        },
        {
            'name': 'Innovation',
            'name_en': 'Innovation',
            'slug': 'innovation',
            'description': 'Technologies et innovations',
            'color': '#F39C12'
        },
        {
            'name': 'Design',
            'name_en': 'Design',
            'slug': 'design',
            'description': 'Design web et UX/UI',
            'color': '#789AA1'
        },
        {
            'name': 'International',
            'name_en': 'International',
            'slug': 'international',
            'description': 'Expansion internationale et multilingue',
            'color': '#2ECC71'
        },
        {
            'name': 'Analytics',
            'name_en': 'Analytics',
            'slug': 'analytics',
            'description': 'Analyses et métriques',
            'color': '#9B59B6'
        }
    ]
    
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            slug=cat_data['slug'],
            defaults=cat_data
        )
        if created:
            print(f"Catégorie créée: {category.name}")
    
    # Create blog posts
    support_category = Category.objects.get(slug='support-client')
    ecommerce_category = Category.objects.get(slug='ecommerce')
    innovation_category = Category.objects.get(slug='innovation')
    design_category = Category.objects.get(slug='design')
    international_category = Category.objects.get(slug='international')
    analytics_category = Category.objects.get(slug='analytics')
    
    blog_posts_data = [
        {
            'title': 'Comment Optimiser Votre Support Client E-commerce en 2024',
            'title_en': 'How to Optimize Your E-commerce Customer Support in 2024',
            'slug': 'optimiser-support-client-ecommerce-2024',
            'content': '<p>Le support client est devenu un élément différenciateur majeur dans l\'e-commerce moderne...</p>',
            'content_en': '<p>Customer support has become a major differentiator in modern e-commerce...</p>',
            'excerpt': 'Découvrez les stratégies avancées pour transformer votre service client en avantage concurrentiel majeur. De l\'automatisation intelligente aux équipes multilingues, explorez les meilleures pratiques qui font la différence.',
            'excerpt_en': 'Discover advanced strategies to transform your customer service into a major competitive advantage. From intelligent automation to multilingual teams, explore best practices that make the difference.',
            'author': admin_user,
            'category': support_category,
            'featured_image': 'https://images.pexels.com/photos/3184338/pexels-photo-3184338.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=2',
            'is_featured': True,
            'read_time': '5 min',
            'tags': ['e-commerce', 'support', 'stratégie', 'optimisation'],
            'tags_en': ['e-commerce', 'support', 'strategy', 'optimization'],
        },
        {
            'title': 'L\'IA dans le Service Client : Révolution ou Evolution ?',
            'title_en': 'AI in Customer Service: Revolution or Evolution?',
            'slug': 'ia-service-client-revolution-evolution',
            'content': '<p>L\'intelligence artificielle transforme progressivement le paysage du service client...</p>',
            'content_en': '<p>Artificial intelligence is gradually transforming the customer service landscape...</p>',
            'excerpt': 'Analyse approfondie de l\'impact de l\'intelligence artificielle sur la relation client moderne. Comment intégrer les chatbots sans perdre l\'aspect humain de votre service.',
            'excerpt_en': 'In-depth analysis of artificial intelligence\'s impact on modern customer relations. How to integrate chatbots without losing the human aspect of your service.',
            'author': admin_user,
            'category': innovation_category,
            'featured_image': 'https://images.pexels.com/photos/8386440/pexels-photo-8386440.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=2',
            'is_featured': False,
            'read_time': '7 min',
            'tags': ['IA', 'technologie', 'futur', 'chatbot'],
            'tags_en': ['AI', 'technology', 'future', 'chatbot'],
        },
        {
            'title': 'Dropshipping : 10 Erreurs à Éviter Absolument',
            'title_en': 'Dropshipping: 10 Mistakes to Absolutely Avoid',
            'slug': 'dropshipping-erreurs-eviter',
            'content': '<p>Le dropshipping peut être très rentable, mais de nombreux entrepreneurs commettent des erreurs coûteuses...</p>',
            'content_en': '<p>Dropshipping can be very profitable, but many entrepreneurs make costly mistakes...</p>',
            'excerpt': 'Guide complet pour éviter les pièges les plus courants du dropshipping et maximiser vos profits. Des conseils pratiques basés sur notre expérience avec plus de 100 marques.',
            'excerpt_en': 'Complete guide to avoid the most common dropshipping pitfalls and maximize your profits. Practical advice based on our experience with over 100 brands.',
            'author': admin_user,
            'category': ecommerce_category,
            'featured_image': 'https://images.pexels.com/photos/4482900/pexels-photo-4482900.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=2',
            'is_featured': False,
            'read_time': '6 min',
            'tags': ['dropshipping', 'conseils', 'business', 'erreurs'],
            'tags_en': ['dropshipping', 'tips', 'business', 'mistakes'],
        },
        {
            'title': 'Tendances Web Design 2024 : Ce Qui Va Marquer l\'Année',
            'title_en': 'Web Design Trends 2024: What Will Mark the Year',
            'slug': 'tendances-web-design-2024',
            'content': '<p>Le design web évolue constamment, et 2024 apporte son lot de nouvelles tendances...</p>',
            'content_en': '<p>Web design is constantly evolving, and 2024 brings its share of new trends...</p>',
            'excerpt': 'Découvrez les tendances design qui vont dominer le web cette année et comment les intégrer dans votre stratégie e-commerce pour maximiser les conversions.',
            'excerpt_en': 'Discover the design trends that will dominate the web this year and how to integrate them into your e-commerce strategy to maximize conversions.',
            'author': admin_user,
            'category': design_category,
            'featured_image': 'https://images.pexels.com/photos/196644/pexels-photo-196644.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=2',
            'is_featured': False,
            'read_time': '4 min',
            'tags': ['design', 'tendances', 'web', 'UX'],
            'tags_en': ['design', 'trends', 'web', 'UX'],
        },
        {
            'title': 'Support Multilingue : Pourquoi Votre Business en a Besoin',
            'title_en': 'Multilingual Support: Why Your Business Needs It',
            'slug': 'support-multilingue-business',
            'content': '<p>Dans un monde de plus en plus connecté, le support multilingue devient essentiel...</p>',
            'content_en': '<p>In an increasingly connected world, multilingual support becomes essential...</p>',
            'excerpt': 'L\'importance cruciale du support multilingue pour conquérir les marchés internationaux. Stratégies et outils pour une expansion réussie.',
            'excerpt_en': 'The crucial importance of multilingual support to conquer international markets. Strategies and tools for successful expansion.',
            'author': admin_user,
            'category': international_category,
            'featured_image': 'https://images.pexels.com/photos/3184465/pexels-photo-3184465.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=2',
            'is_featured': False,
            'read_time': '5 min',
            'tags': ['multilingue', 'international', 'croissance', 'expansion'],
            'tags_en': ['multilingual', 'international', 'growth', 'expansion'],
        },
        {
            'title': 'ROI du Support Client : Comment Mesurer l\'Impact',
            'title_en': 'Customer Support ROI: How to Measure Impact',
            'slug': 'roi-support-client-mesurer-impact',
            'content': '<p>Mesurer le retour sur investissement du support client est crucial pour justifier les budgets...</p>',
            'content_en': '<p>Measuring customer support ROI is crucial to justify budgets...</p>',
            'excerpt': 'Méthodes et outils pour calculer précisément le retour sur investissement de votre support client. KPIs essentiels et tableaux de bord performants.',
            'excerpt_en': 'Methods and tools to accurately calculate the return on investment of your customer support. Essential KPIs and performance dashboards.',
            'author': admin_user,
            'category': analytics_category,
            'featured_image': 'https://images.pexels.com/photos/590022/pexels-photo-590022.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=2',
            'is_featured': False,
            'read_time': '8 min',
            'tags': ['ROI', 'analytics', 'performance', 'KPI'],
            'tags_en': ['ROI', 'analytics', 'performance', 'KPI'],
        },
        {
            'title': 'Black Friday 2024 : Préparer Votre Support Client',
            'title_en': 'Black Friday 2024: Preparing Your Customer Support',
            'slug': 'black-friday-2024-preparer-support',
            'content': '<p>Le Black Friday représente un défi majeur pour les équipes de support client...</p>',
            'content_en': '<p>Black Friday represents a major challenge for customer support teams...</p>',
            'excerpt': 'Guide complet pour anticiper et gérer l\'afflux de demandes pendant les périodes de forte activité. Checklist et bonnes pratiques.',
            'excerpt_en': 'Complete guide to anticipate and manage the influx of requests during high activity periods. Checklist and best practices.',
            'author': admin_user,
            'category': ecommerce_category,
            'featured_image': 'https://images.pexels.com/photos/5632402/pexels-photo-5632402.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=2',
            'is_featured': False,
            'read_time': '6 min',
            'tags': ['black-friday', 'préparation', 'pic-activité', 'stratégie'],
            'tags_en': ['black-friday', 'preparation', 'peak-activity', 'strategy'],
        },
        {
            'title': 'WordPress vs Shopify : Quel CMS Choisir en 2024 ?',
            'title_en': 'WordPress vs Shopify: Which CMS to Choose in 2024?',
            'slug': 'wordpress-vs-shopify-cms-2024',
            'content': '<p>Le choix du CMS est crucial pour le succès de votre e-commerce...</p>',
            'content_en': '<p>Choosing the right CMS is crucial for your e-commerce success...</p>',
            'excerpt': 'Comparatif détaillé entre WordPress et Shopify pour votre e-commerce. Avantages, inconvénients et critères de choix selon votre business.',
            'excerpt_en': 'Detailed comparison between WordPress and Shopify for your e-commerce. Advantages, disadvantages and selection criteria according to your business.',
            'author': admin_user,
            'category': design_category,
            'featured_image': 'https://images.pexels.com/photos/265087/pexels-photo-265087.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&dpr=2',
            'is_featured': False,
            'read_time': '7 min',
            'tags': ['wordpress', 'shopify', 'CMS', 'comparatif'],
            'tags_en': ['wordpress', 'shopify', 'CMS', 'comparison'],
        }
    ]
    
    for post_data in blog_posts_data:
        post, created = BlogPost.objects.get_or_create(
            slug=post_data['slug'],
            defaults=post_data
        )
        if created:
            print(f"Article créé: {post.title}")
    
    print("Données du blog créées avec succès!")

if __name__ == '__main__':
    populate_blog_data()