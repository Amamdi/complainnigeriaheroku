# Generated by Django 3.1.6 on 2021-02-20 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naijacomplainer', '0007_complainer_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='complainer',
            options={'ordering': ['-id']},
        ),
        migrations.RemoveField(
            model_name='complainer',
            name='message',
        ),
        migrations.RemoveField(
            model_name='complainer',
            name='sector',
        ),
        migrations.AddField(
            model_name='complainer',
            name='complaint',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='complainer',
            name='complaintIsAgainst',
            field=models.CharField(choices=[('Federal Government', 'Federal Government'), ('State Government', 'State Government'), ('Local Government', 'Local Government'), ('Private Company', 'Private Company'), ('Public Company', 'Public Company'), ('Other', 'Other')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='complainer',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='complainer',
            name='natureOfComplaint',
            field=models.CharField(choices=[('Delay of Service', 'Delay of Service'), ('Non compliance with Regulation', 'Non compliance with Regulation'), ('Demand for Bribery', 'Demand for Bribery'), ('Vandalism', 'Vandalism'), ('Unrepaired or damaged infrastructure', 'Unrepaired or damaged infrastructure '), ('Insecurity', 'Insecurity'), ('Non Payment of Salary', 'Non Payment of Salary'), ('Other', 'Other')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='complainer',
            name='state',
            field=models.CharField(choices=[('Abia', 'Abia'), ('Abuja', 'Abuja'), ('Adamawa', 'Adamawa'), ('Akwa-Ibom', 'Akwa-Ibom'), ('Anambra', 'Anambra'), ('Bauchi', 'Bauchi'), ('Bayelsa', 'Bayelsa'), ('Benue', 'Benue'), ('Borno', 'Borno'), ('Cross-River', 'Cross-River'), ('Delta', 'Delta'), ('Ebonyi', 'Ebonyi'), ('Edo', 'Edo'), ('Ekiti', 'Ekiti'), ('Enugu', 'Enugu'), ('Gombe', 'Gombe'), ('Imo', 'Imo'), ('Jigawa', 'Jigawa'), ('Kaduna', 'Kaduna'), ('Kano', 'Kano'), ('Katsina', 'Katsina'), ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'), ('Kwara', 'Kwara'), ('Lagos', 'Lagos'), ('Nasarawa', 'Nasarawa'), ('Niger', 'Niger'), ('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('Osun', 'Osun'), ('Oyo', 'Oyo'), ('Plateau', 'Plateau'), ('Rivers', 'Rivers'), ('Sokoto', 'Sokoto'), ('Taraba', 'Taraba'), ('Yobe', 'Yobe'), ('Zamfara', 'Zamfara')], max_length=20),
        ),
    ]