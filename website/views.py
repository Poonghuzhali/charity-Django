from django.shortcuts import redirect, render


def home(request):
    causes = [
        {
            'title': 'Education for Children',
            'description': (
                'We provide access to quality education, school supplies, '
                'and learning opportunities for underprivileged children.'
            ),
            'image': 'website/images/cause-education.png',
        },
        {
            'title': 'Medical Support',
            'description': (
                'Our medical programs deliver essential healthcare, '
                'medicines, and wellness support to communities in need.'
            ),
            'image': 'website/images/cause-medical.png',
        },
        {
            'title': 'Food & Shelter',
            'description': (
                'We ensure families have nutritious meals and safe shelter '
                'during times of hardship and displacement.'
            ),
            'image': 'website/images/cause-shelter.png',
        },
        {
            'title': 'Disaster Relief',
            'description': (
                'When disaster strikes, we respond quickly with emergency '
                'aid, supplies, and long-term recovery assistance.'
            ),
            'image': 'website/images/cause-disaster.png',
        },
    ]

    impact_stats = [
        {'label': 'Lives Helped', 'value': '10,000+'},
        {'label': 'Volunteers', 'value': '500+'},
        {'label': 'Projects Completed', 'value': '120+'},
    ]

    testimonials = [
        {
            'name': 'Sophia Carter',
            'date': '2023-08-15',
            'avatar': 'website/images/avatar-1.png',
            'text': (
                'HopeHands Foundation changed my life. Their support helped '
                'my family through the toughest times. I am forever grateful '
                'for their kindness and dedication.'
            ),
            'likes': 24,
            'dislikes': 2,
        },
        {
            'name': 'Ethan Bennett',
            'date': '2023-07-22',
            'avatar': 'website/images/avatar-2.png',
            'text': (
                'Volunteering with HopeHands has been incredibly rewarding. '
                'Seeing the direct impact of our work in local communities '
                'reminds me why giving back matters so much.'
            ),
            'likes': 18,
            'dislikes': 1,
        },
        {
            'name': 'Olivia Hayes',
            'date': '2023-09-03',
            'avatar': 'website/images/avatar-3.png',
            'text': (
                'The medical support program provided my village with '
                'essential care we could never have afforded. HopeHands '
                'truly lives up to its name.'
            ),
            'likes': 31,
            'dislikes': 0,
        },
    ]

    context = {
        'active_page': 'home',
        'causes': causes,
        'impact_stats': impact_stats,
        'testimonials': testimonials,
    }
    return render(request, 'website/home.html', context)


def about(request):
    values = [
        {
            'title': 'Compassion',
            'description': (
                'We lead with empathy, treating every individual with dignity '
                'and responding to their needs with genuine care and understanding.'
            ),
            'icon': 'website/images/icon-compassion.svg',
        },
        {
            'title': 'Collaboration',
            'description': (
                'We believe lasting change happens together. We partner with '
                'communities, volunteers, and organizations to amplify our impact.'
            ),
            'icon': 'website/images/icon-collaboration.svg',
        },
        {
            'title': 'Integrity',
            'description': (
                'We uphold the highest standards of honesty and accountability, '
                'ensuring every resource is used ethically and transparently.'
            ),
            'icon': 'website/images/icon-integrity.svg',
        },
    ]

    team_members = [
        {
            'name': 'Sarah Johnson',
            'role': 'Co-Founder & Executive Director',
            'avatar': 'website/images/team-sarah.png',
        },
        {
            'name': 'David Lee',
            'role': 'Co-Founder & Director of Programs',
            'avatar': 'website/images/team-david.png',
        },
        {
            'name': 'Emily Carter',
            'role': 'Head of Community Outreach',
            'avatar': 'website/images/team-emily.png',
        },
    ]

    context = {
        'active_page': 'about',
        'values': values,
        'team_members': team_members,
    }
    return render(request, 'website/about.html', context)


def causes(request):
    causes_list = [
        {
            'slug': 'healthcare-for-children',
            'title': 'Healthcare for Children',
            'description': (
                'Many children lack access to basic healthcare, leading to preventable '
                'diseases and suffering. We aim to bridge this gap by providing comprehensive '
                'medical support. Your donation will help provide essential medical care, '
                'including surgeries, treatments, and rehabilitation, to children suffering '
                'from critical illnesses.'
            ),
            'image': 'website/images/cause-healthcare.png',
        },
        {
            'slug': 'education-for-all',
            'title': 'Education for All',
            'description': (
                'Education is a fundamental right, yet many children are deprived of it due '
                'to poverty. We strive to provide quality education and resources to these '
                'children. Your support will fund educational programs, school supplies, and '
                'mentorship opportunities for underprivileged children, helping them achieve '
                'their full potential.'
            ),
            'image': 'website/images/cause-education-all.png',
        },
        {
            'slug': 'poverty-relief',
            'title': 'Poverty Relief',
            'description': (
                'Poverty affects millions, leading to hunger, homelessness, and lack of basic '
                'necessities. We work to alleviate poverty by providing essential resources and '
                'support. Your contribution will help us provide nutritious meals, clean water, '
                'and safe shelter to families struggling with poverty, ensuring their basic '
                'needs are met.'
            ),
            'image': 'website/images/cause-poverty.png',
        },
        {
            'slug': 'environmental-sustainability',
            'title': 'Environmental Sustainability',
            'description': (
                'Protecting our planet is crucial for future generations. We focus on '
                'environmental conservation and sustainability to ensure a healthy world for '
                'all. Your donation will support our efforts to protect the environment, '
                'promote sustainable practices, and raise awareness about climate change.'
            ),
            'image': 'website/images/cause-environment.png',
        },
    ]

    context = {
        'active_page': 'causes',
        'causes': causes_list,
    }
    return render(request, 'website/causes.html', context)


def donate(request):
    cause_options = [
        {'slug': 'healthcare-for-children', 'title': 'Healthcare for Children'},
        {'slug': 'education-for-all', 'title': 'Education for All'},
        {'slug': 'poverty-relief', 'title': 'Poverty Relief'},
        {'slug': 'environmental-sustainability', 'title': 'Environmental Sustainability'},
    ]

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        address = request.POST.get('address', '').strip()
        cause = request.POST.get('cause', '').strip()
        amount = request.POST.get('amount', '').strip()

        valid_causes = {c['slug'] for c in cause_options}
        amount_int = int(amount) if amount.isdigit() else 0

        if name and email and address and cause in valid_causes and amount_int > 0:
            request.session['last_donation'] = {
                'name': name,
                'email': email,
                'amount': amount_int,
                'cause': cause,
            }
            return redirect('thank_you')

    context = {
        'active_page': 'donate',
        'cause_options': cause_options,
        'donation_amounts': [500, 1000, 2000],
        'selected_cause': request.GET.get('cause', '') or request.POST.get('cause', ''),
    }
    return render(request, 'website/donate.html', context)


def contact(request):
    contact_info = [
        {
            'type': 'email',
            'value': 'support@hopehands.org',
            'href': 'mailto:support@hopehands.org',
        },
        {
            'type': 'phone',
            'value': '+91 98765 43210',
            'href': 'tel:+919876543210',
        },
        {
            'type': 'location',
            'value': 'Chennai, India',
            'href': '',
        },
    ]

    trust_badges = [
        {'label': 'Trusted by Volunteers', 'color': 'green', 'icon': 'shield'},
        {'label': 'Community Support', 'color': 'blue', 'icon': 'community'},
        {'label': 'Making a Difference', 'color': 'red', 'icon': 'heart'},
    ]

    context = {
        'active_page': 'contact',
        'contact_info': contact_info,
        'trust_badges': trust_badges,
    }
    return render(request, 'website/contact.html', context)


def volunteer(request):
    ways_to_help = [
        {'title': 'Education Support', 'color': 'blue', 'icon': 'education'},
        {'title': 'Medical Assistance', 'color': 'green', 'icon': 'medical'},
        {'title': 'Food Distribution', 'color': 'orange', 'icon': 'food'},
        {'title': 'Event Coordination', 'color': 'purple', 'icon': 'event'},
        {'title': 'Online / Remote Volunteering', 'color': 'cyan', 'icon': 'remote'},
    ]

    interest_options = [way['title'] for way in ways_to_help]
    availability_options = [
        'Weekdays',
        'Weekends',
        'Evenings Only',
        'Flexible / Part-time',
        'Full-time',
    ]

    context = {
        'active_page': 'volunteer',
        'ways_to_help': ways_to_help,
        'interest_options': interest_options,
        'availability_options': availability_options,
    }
    return render(request, 'website/volunteer.html', context)


def thank_you(request):
    impact_items = [
        {
            'title': 'Educated a child for a month',
            'description': (
                'Your contribution ensures a child receives quality education for an entire month.'
            ),
            'image': 'website/images/impact-education.png',
        },
        {
            'title': 'Provided meals for families',
            'description': (
                'Your donation helps provide nutritious meals to families in need.'
            ),
            'image': 'website/images/impact-meals.png',
        },
        {
            'title': 'Supported basic healthcare',
            'description': (
                'Your support aids in delivering essential healthcare services to those without access.'
            ),
            'image': 'website/images/impact-healthcare.png',
        },
    ]

    context = {
        'active_page': 'thank_you',
        'impact_items': impact_items,
    }
    return render(request, 'website/thankyou.html', context)
