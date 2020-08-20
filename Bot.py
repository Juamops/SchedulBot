import discord
from discord.ext import commands
import datetime as dt


token = 'INSERT_TOKEN_HERE'
client = commands.Bot(command_prefix='#')
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('With Schedules'))
    print('Bot is ready!')

@client.event
async def on_member_join(member):
    print(f'{member}, has joined the server.')

@client.command()
async def schedule(ctx):

    sched_only = '#schedule'
    period = getCurrentPeriod()

    if (ctx.message.content == sched_only):
        await ctx.send(f'You have: {get_message(user=ctx.author.id, period=period)}')

    elif (len(ctx.message.mentions) == 1 and len(ctx.message.content.split(' ')) == 2):
        await ctx.send(f'{ctx.message.mentions[0].name} has: {get_message(user=ctx.message.mentions[0].id, period=period)}')

    elif (ctx.message.content.split(' ')[1] == 'zoom'):

        if (period == 0):
            await ctx.send(f'{get_message(user=ctx.author.id, period=period)}')

        else:
            await ctx.send(f'The Zoom Link for {get_message(user=ctx.author.id, period=period)} is: '
                           f'{get_zoom(clss=get_message(user=ctx.author.id, period=period), period=period)}')

    elif (ctx.message.content.split(' ')[2] == 'zoom'):

        if (period == 0):
            await ctx.send(f'{get_message(user=ctx.message.mentions[0].id, period=period)}')

        else:
            await ctx.send(
                f'The Zoom Link for {get_message(user=ctx.message.mentions[0].id, period=period)} is: '
                f'{get_zoom(clss=get_message(user=ctx.message.mentions[0].id, period=period), period=period)}')

    print('"Schedule" was used by: ' + ctx.message.author)

@client.command()
async def register(ctx):
    await ctx.send(f'Thank you for registering {ctx.author.name}')
    print(f'{ctx.author.name} id is: {ctx.author.id}')


@client.command()
async def help(ctx):

    embed = discord.Embed(
        title = 'Help',
        description = 'The listing of all functional commands',
        color = discord.Color.red()
    )

    embed.set_footer(text='Have fun little kid')
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/745683424215433319/233218136e7acd37e4b9724086b25f75.png?size=256')
    embed.add_field(name='#schedule', value='This is the initializer, always type this to begin a command.',inline=True)
    embed.add_field(name='#register', value='Only do this when Juamops instructs you to.',inline=True)
    embed.add_field(name='#help', value='This is the command you just used (it shows this)', inline=True)
    embed.add_field(name='@user', value='Mention someone to refer to their Schedule.',inline=True)
    embed.add_field(name='zoom', value='Use this to get the Zoom Link to the current class',inline=True)

    await ctx.send(embed = embed)
    print('"Help" was used by: ' + ctx.message.author)

def getCurrentPeriod():
    date = dt.datetime.now()
    time = str(date).split(' ')[1].split('.')[0]
    day = date.weekday()
    period = 0

    if (day == 0):

        if (int(time.split(':')[0]) == 8 and int(time.split(':')[1]) >= 20 and
                int(time.split(':')[0]) <= 9 and int(time.split(':')[1]) < 50 ):
            period = 1

        elif (int(time.split(':')[0]) == 9 and int(time.split(':')[1]) >= 50 and
                int(time.split(':')[0]) <= 11 and int(time.split(':')[1]) < 20):
            period = 2

        elif (int(time.split(':')[0]) == 12 and int(time.split(':')[1]) >= 0 and
              int(time.split(':')[0]) <= 13 and int(time.split(':')[1]) < 30):
            period = 3

        elif (int(time.split(':')[0]) == 13 and int(time.split(':')[1]) >= 30 and
              int(time.split(':')[0]) <= 15 and int(time.split(':')[1]) < 0):
            period = 4

        else:
            period = 0

    elif (day == 1):

        if (int(time.split(':')[0]) == 8 and int(time.split(':')[1]) >= 20 and
                int(time.split(':')[0]) <= 9 and int(time.split(':')[1]) < 30):
            period = 5

        elif (int(time.split(':')[0]) == 9 and int(time.split(':')[1]) >= 50 and
              int(time.split(':')[0]) <= 11 and int(time.split(':')[1]) < 20):
            period = 6

        elif (int(time.split(':')[0]) == 12 and int(time.split(':')[1]) >= 0 and
              int(time.split(':')[0]) <= 13 and int(time.split(':')[1]) < 30):
            period = 7

        elif (int(time.split(':')[0]) == 13 and int(time.split(':')[1]) >= 30 and
              int(time.split(':')[0]) <= 14 and int(time.split(':')[1]) < 15):
            period = 8

        else:
            period = 0

    elif (day == 2):

        period = 0

    elif (day == 3):

        if (int(time.split(':')[0]) == 8 and int(time.split(':')[1]) >= 20 and
                int(time.split(':')[0]) <= 9 and int(time.split(':')[1]) < 30):
            period = 4

        elif (int(time.split(':')[0]) == 9 and int(time.split(':')[1]) >= 90 and
              int(time.split(':')[0]) <= 11 and int(time.split(':')[1]) < 20):
            period = 3

        elif (int(time.split(':')[0]) == 12 and int(time.split(':')[1]) >= 0 and
              int(time.split(':')[0]) <= 13 and int(time.split(':')[1]) < 30):
            period = 2

        elif (int(time.split(':')[0]) == 13 and int(time.split(':')[1]) >= 30 and
              int(time.split(':')[0]) <= 15 and int(time.split(':')[1]) < 0):
            period = 1

        else:
            period = 0

    elif (day == 4):

        if (int(time.split(':')[0]) == 8 and int(time.split(':')[1]) >= 20 and
                int(time.split(':')[0]) <= 9 and int(time.split(':')[1]) < 30):
            period = 7

        elif (int(time.split(':')[0]) == 9 and int(time.split(':')[1]) >= 50 and
              int(time.split(':')[0]) <= 10 and int(time.split(':')[1]) < 35):
            period = 8

        elif (int(time.split(':')[0]) == 12 and int(time.split(':')[1]) >= 0 and
              int(time.split(':')[0]) <= 13 and int(time.split(':')[1]) < 30):
            period = 6

        elif (int(time.split(':')[0]) == 13 and int(time.split(':')[1]) >= 30 and
              int(time.split(':')[0]) <= 15 and int(time.split(':')[1]) == 0):
            period = 5

        else:
            period = 0

    else:
        period = 0

    return period


def get_message(user, period):

    zilbera = 547856238067580928
    soulsurge = 396354178357788674
    ethereal = 614441419393728512
    quieres = 531253369575309352
    rikki = 580464781912309760
    jpshavz = 639944521651847188
    juamops = 335117740001984515
    eddycross = 699034606250360914

    user_dict = {}
    message = ''

    if(user == jpshavz):
        #JP
        user_dict = {
            1: 'English',
            2: 'Honors Geometry',
            3: 'PE',
            4: 'Spanish',
            5: 'Chemistry',
            6: 'History/Civics',
            7: 'AP Human Geography',
            8: 'Mentoring'
        }

    if (user == zilbera):
        #Zilbera
        user_dict = {
            1: 'CP Geometry',
            2: 'Chemistry',
            3: 'Programming',
            4: 'SSL',
            5: 'World History',
            6: 'English',
            7: 'Computer Science',
            8: 'Mentoring'
        }

    if (user == soulsurge):
        #Soulsurge
        user_dict = {
            1: 'Spanish',
            2: 'English',
            3: 'PE',
            4: 'History/Civics',
            5: 'Chemistry',
            6: 'AP Human Geography',
            7: 'CP Geometry',
            8: 'Mentoring'
        }

    if (user == quieres):
        #Quieres?
        user_dict = {
            1: 'English',
            2: 'History/Civics',
            3: 'PE',
            4: 'Spanish',
            5: 'CP Geometry',
            6: 'AP Human Geography',
            7: 'Chemistry',
            8: 'Mentoring'
    }

    if (user == ethereal):
        #Maksym
        user_dict = {
            1: 'Drawing',
            2: 'English',
            3: 'PE',
            4: 'SSL',
            5: 'World History',
            6: 'Chemistry',
            7: 'Computer Science',
            8: 'Mentoring'
        }

    if (user == juamops):
        #Juamops
        user_dict = {
            1: 'English',
            2: 'Honors Geometry',
            3: 'PE',
            4: 'History/Civics',
            5: 'Chemistry',
            6: 'Spanish',
            7: 'World History',
            8: 'Mentoring'
        }

    if (user == rikki):
        #Ricky
        user_dict = {
            1: 'English',
            2: 'Honors Geometry',
            3: 'PE',
            4: 'Chemistry',
            5: 'History/Civics',
            6: 'AP Human Geography',
            7: 'Spanish',
            8: 'Mentoring'
        }

    if (user == eddycross):
        #Edu
        user_dict = {
            1: 'CP Geometry',
            2: 'Spanish',
            3: 'Drama',
            4: 'Chemistry',
            5: 'History/Civics',
            6: 'English',
            7: 'AP Human Geography',
            8: 'Mentoring'
        }



    if (period != 0):
        message = user_dict[period]

    else:
        message = 'There is no active period right now'

    return message

def get_zoom(clss, period):

    tagger = ''

    zoom_links = {
        'English': 'https://zoom.us/j/92486355328',
        'Honors Geometry': 'https://zoom.us/j/91510550409',
        'CP Geometry': 'http://asfg.zoom.us/my/evapetocz',
        'PE': 'https://us04web.zoom.us/j/78994899072?pwd=dDZPZCtUdGkvNUFReDdmQzZXVUpDZz09 PassCode: 83riEn',
        'Programming': 'No Link Yet!',
        'Chemistry': 'https://zoom.us/j/6842856169',
        'Spanish P6': 'https://zoom.us/j/94454930902?pwd=WkZ1aG9UVGlzOXR5ZmhPSUpIQWJxQT09 PassCode: 702714',
        'Spanish P4': 'https://zoom.us/j/97444283237 PassCode: 411715',
        'Spanish P1': 'https://zoom.us/j/93362871535?pwd=L0FzWjJQWkVUbFhhUUlXbGJEVm9MUT09 PassCode: 340584',
        'World History': 'https://zoom.us/j/3224597852',
        'AP Human Geography': 'https://zoom.us/j/91699393495 PassCode: 960317',
        'SSL': 'No Link Yet!',
        'Mentoring': 'This Feature Will be Added Shortly!'
    }

    if (clss == 'Spanish'):
        tagger = f'{clss} P{period}'
    else:
        tagger = clss

    return zoom_links[tagger]






client.run(token)