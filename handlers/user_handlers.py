from aiogram import Router, Bot, F, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, FSInputFile, LabeledPrice, PreCheckoutQuery, BotCommand, InlineQuery, InputInvoiceMessageContent
from lexicon import LEXICON
from aiogram.enums import ParseMode
import uuid

router = Router()


@router.callback_query(F.data == 'stars_pay_pressed')
async def starpay(callback: CallbackQuery):
      await callback.message.answer('If you want to buy access to VIP channel:\n'
                           'Just press on -> /pay \n'
                           'Write to the admin if you have any question💓')

@router.inline_query()
async def show_user_links(inline_query: InlineQuery):
    results = [types.InlineQueryResultArticle(
        id=str(uuid.uuid4()),
        url='https://telegra.ph/file/d30bac6f9503720e89181.jpg',
        thumbnail_url='https://telegra.ph/file/d30bac6f9503720e89181.jpg',
        title="R60GB !VIP!",
        description='FootFetish VIP | R60GB',
        input_message_content=InputInvoiceMessageContent(    
            title='FootFetish VIP | R60GB',
            description='3700+ Media🔥\n\n'
            '🐾60+ models🐾\n\n'
            'content replenishment every day!⚡\n'
            '⭐the BEST footfetish VIP channel in the world⭐\n'
            'you can look at the examples for free:\n\n'
            'https://t.me/+pKPXSJPKtEE3ZDMy',
            prices=[LabeledPrice(label="XTR", amount=250)],
            provider_token="",
            payload='25',
            currency="XTR",
            photo_url='https://telegra.ph/file/d30bac6f9503720e89181.jpg'))]
    
    await inline_query.answer(results, cache_time=1)
    

@router.pre_checkout_query()
async def on_pre_checkout_query(
    pre_checkout_query: PreCheckoutQuery):
    await pre_checkout_query.answer(ok=True)

@router.message(F.successful_payment)
async def on_successful_payment(message: Message):
    await message.answer("payment-successful\n\n LINK - https://t.me/+N5n3qEC1Db1mY2Qy")

@router.message(F.content_type.in_({'photo', 'video', 'file'}))
async def forward_massage(message: types.Message, bot: Bot):
       await bot.forward_message(-1002191268370, message.from_user.id, message.message_id)
       await bot.send_message(text='Thank you!\n\n' 
                              'Your message has been sent.')

@router.callback_query(F.data == 'predlozhka_button_pressed')
async def preeedlozhka(callback: CallbackQuery):
       await callback.message.answer(text='You can send a photo/video/file right now and here '
                                     'so that I can post it if it fits.\n\n' 
                                     'Thank you in advance for this, as it saves me a lot of time!')

@router.callback_query(F.data == 'check_channels_button_pressed')
async def start(callback: CallbackQuery):
    await callback.message.answer(text="<b>To get free content you must be subscribed\n"
                                "to ALL of our channels, you can subscribe to them\n" 
                                "with one click on this link</b> 👇👇👇\n\n https://t.me/addlist/_0K1G6A89RoxNTVi",
                                   reply_markup=check_sub_key, 
                                   parse_mode='HTML')



@router.callback_query(F.data == 'check_sub_button_pressed')
async def cheeeeck(message: types.Message, bot: Bot):
        sub = await bot.get_chat_member(chat_id='@tiktok_feet', user_id=message.from_user.id)
        if sub.status != 'left':
            await bot.send_message(text='LINK - https://t.me/+NucoCAAmSfY2N2Q6', chat_id=message.from_user.id)
        else:
            await bot.send_message(text='<b>To access 18+ content</b>, you must\n be subscribed to <b>all of our channels</b>.\n\n Do it with a single tap👇👇👇\n\n https://t.me/addlist/_0K1G6A89RoxNTVi', 
                                     parse_mode=ParseMode.HTML,
                                     chat_id=message.from_user.id,
                                     reply_markup=check_sub_key
                                     )
             
@router.message(Command('start'))
async def process_start(message: Message, bot: Bot):
    await message.answer(
    text=LEXICON['/start'], 
    reply_markup=catalog_keyboard,
    parse_mode=ParseMode.HTML
    )
    await bot.send_sticker(message.from_user.id, sticker='CAACAgUAAxkBAAEMjKpmpLpA8A-l2LH2hS2OHdM7JqacbgACtg4AAvseyFUFGbhanaCfRDUE')
    
main_menu_commands = [
        BotCommand(command='/help',
                   description='Bot Info, FAQ, support'),
        BotCommand(command='/buy_footfetish_vip',
                   description='FootFetishVIP | R60GB'),
        BotCommand(command='/buy_hentaifeet_vip',
                   description='HentaiFeet VIP | R60GB'),
        BotCommand(command='/dual_access',
                   description='FootFet VIP + HentFeet VIP (big discount)')
    ]


@router.message(Command('help'))
async def heeelp(message: Message):
       await message.answer(LEXICON['/help'])


@router.message(Command('buy_footfetish_vip'))
async def create_invoice(message: Message):
       await message.answer_invoice(
                            title='FootFetish VIP +18 | R60GB',
                            description='FootFetish VIP\n\n' 
            '3700+ media\n\n' 
            '60+ Onlyfans&Footfetish Models Leak\n\n'
            'Popular Hashtags: teens, footjob, selfworship, '
            'ballbusting, footgagging, tickling, femdom, bootjob '
            'and 60 hashtags more...\n' 
            'You can look at the examples:\n\n'
            'https://t.me/+pKPXSJPKtEE3ZDMy\n',
                            payload='payload',
                            currency='XTR',
                            prices=[
                                    LabeledPrice(label='label',
                                                 amount=250)],
                            provider_token='teeeeeeest',
                            photo_url='https://telegra.ph/file/c1bbf38e1efee9ab509b6.jpg',
                            photo_height=800,
                            photo_width=900
                                                 )


@router.message(Command('buy_hentaifeet_vip'))
async def create_invoicee(message: Message):
       await message.answer_invoice(
                            title='HentaiFeet VIP +18 | R60GB',
                            description='Hentai FootFetish(+18)\n\n1000+ Media,\n\ncontent replenishment every day!⚡\n\nYou can look at the free examples:\nhttps://t.me/+s8-fSGmvW6E5NTIy\n\n',
                            payload='payloadd',
                            currency='XTR',
                            prices=[
                                    LabeledPrice(label='label',
                                                 amount=250)],
                            provider_token='teeeeeeesasat',
                            photo_url='https://telegra.ph/file/6b76f706ee50bce76b9db.jpg',
                            photo_height=800,
                            photo_width=900
                                                 )


@router.message(Command('dual_access'))
async def create_invoicee(message: Message):
       await message.answer_invoice(
                            title='HentaiFeet VIP + FootFetish VIP | R60GB',
                            description='Hentai FootFetish(+18)\n\n1000+ Media\ncontent replenishment every day!⚡\nYou can look at the free examples:\nhttps://t.me/+pNJlKl0pplplOTZi\n\n'
                            'FootFetish VIP | R60GB,\n\n 3700+ Media🔥, 🐾60+ models🐾, content replenishment every day!⚡\n⭐the BEST footfetish VIP /more channel in the world⭐,\nyou can look at the examples for free:\nhttps://t.me/+pKPXSJPKtEE3ZDMy',
                            payload='payloadd',
                            currency='XTR',
                            prices=[
                                    LabeledPrice(label='label',
                                                 amount=420)],
                            provider_token='teeeeeeesasat',
                            photo_url='https://telegra.ph/file/9152e5bc24092fe9bc7b9.jpg',
                            photo_height=800,
                            photo_width=900
                                                 )

@router.message(Command('more'))
async def heeelp(message: Message):
       await message.answer('channel in the world⭐,\nyou can look at the examples for free:\nhttps://t.me/+pKPXSJPKtEE3ZDMy')

@router.pre_checkout_query()
async def checkout_handler(checkout_query: PreCheckoutQuery):
       await checkout_query.answer(ok=True)

@router.message(F.successful_payment)
async def star_payment(message: Message):
       await message.answer('LINK - https://t.me/+y3Is9nPOPsswZGUy')


@router.message(Command('pay'))
async def heeelp(message: Message):
       await message.answer('Choose your tarif:\n\n/buy_footfetish_vip - FootFetish VIP(+18)\n\n/buy_hentaifeet_vip - HentaiFeet VIP(+18)\n\n/dual_access - HentaiFeet VIP + FootFetish VIP (DISCOUNT!)\n\n (click on the link)')



@router.callback_query(F.data == 'hent_oplata_button_pressed')
async def processhent(callback: CallbackQuery):
        await callback.message.answer(
        text='You can pay with:',
        reply_markup=method_oplata_hent, 
                                   parse_mode='HTML'
    )

@router.callback_query(F.data == 'Hent_feet_button_pressed')
async def hent_catalog(message: Message, bot: Bot):
      await bot.send_photo(chat_id=message.from_user.id, caption=LEXICON['ffanime'],
        reply_markup=b_t_s_keyboard_ifphoto_hentai,
        photo=FSInputFile('photo_5327967795125805124_y.jpeg'),
        parse_mode='HTML')

@router.callback_query(F.data == 'ffvip_button_pressed')
async def process_photo_iphone(message: Message, bot: Bot):
    await bot.send_photo(chat_id=message.from_user.id, caption=LEXICON['awesfeet'], 
        reply_markup=b_t_s_keyboard_ifphoto,
        photo=FSInputFile('photo_5327967795125805123_y.jpeg'), 
                                   parse_mode='HTML'
    )

@router.callback_query(F.data == 'back_to_start_button_pressed')
async def back_to_start(callback: CallbackQuery):
        await callback.message.answer(text=LEXICON['/start'], 
        reply_markup=catalog_keyboard, 
                                   parse_mode='HTML'
                                     )
@router.callback_query(F.data == 'oplata_button_pressed')
async def oplata(callback: CallbackQuery):
        await callback.message.answer(
        text='Choose your tarif:\n\n'
        '/buy_footfetish_vip - FootFetish VIP(+18)\n\n/buy_hentaifeet_vip - HentaiFeet VIP(+18)\n\n/dual_access - HentaiFeet VIP + FootFetish VIP (DISCOUNT!)\n\n(click on the link)', 
                                   parse_mode='HTML'
    )
@router.callback_query(F.data == 'b_t_s_button_ifphoto_pressed')
async def b_t_s_ifphoto(callback: CallbackQuery):
        await callback.message.answer(
        text='<b>Catalog of products in stock:</b>',
        reply_markup=keyboard,
        parse_mode='HTML'
    )
        
@router.callback_query(F.data == 'hentvip_button_pressed') #5
async def process_photo_iphone(message: Message, bot: Bot):
        await bot.send_photo(chat_id=message.from_user.id ,caption=
        LEXICON['ffanime'],
        reply_markup=b_t_s_keyboard_ifphoto_hentai,
        photo=FSInputFile('photo_5327967795125805124_y.jpeg'), 
                                   parse_mode='HTML'
    )
@router.callback_query(F.data == 'catalog_button_pressed') #ourprivatechannels(2)
async def process_catalog(callback: CallbackQuery):
        await callback.message.edit_text(
        text='<b>Catalog of products in stock:</b>',
        reply_markup=keyboard, 
                                   parse_mode='HTML'
    )
        
@router.callback_query(F.data == 'admin_button_pressed') #3buyaccess
async def process_rerere(callback: CallbackQuery):
        await callback.message.edit_text(
        text=LEXICON['admin_contact'],
        reply_markup=back_to_start_keyboard, 
                                   parse_mode='HTML'
    )
@router.callback_query(F.data == 'perevod_button_pressed')
async def perevodik(callback: CallbackQuery):
        await callback.message.edit_text(
        text=LEXICON['ru_pay'], 
                                   parse_mode='HTML'
    )

@router.callback_query(F.data == 'TOTALVIP_button_pressed')
async def allCHANNELS(message: Message, bot: Bot):
       await bot.send_photo(chat_id=message.from_user.id, caption=LEXICON['TOTAL_CHANNELS'], 
        photo=FSInputFile('photo1717494343.jpeg'), 
        parse_mode='HTML'
                                  )
       
predlozhka_button = InlineKeyboardButton(
       text='Suggest',
       callback_data='predlozhka_button_pressed'
)

check_sub_button = InlineKeyboardButton(
       text='CHECK',
       callback_data='check_sub_button_pressed'
)

oplata_button = InlineKeyboardButton(
    text='Buy🛒',
    callback_data='oplata_button_pressed'
) 
hent_oplata_button = InlineKeyboardButton(
       text='Buy🛒',
       callback_data='hent_oplata_button_pressed'
)
perevod_button = InlineKeyboardButton(
    text='🇷🇺Russian Cards🇷🇺',
    callback_data='perevod_button_pressed'
)

channels_button = InlineKeyboardButton(
    text='Subscribe to all our channels😏',
    url='https://t.me/addlist/_0K1G6A89RoxNTVi'
)

Hent_feet_button = InlineKeyboardButton(
      text='👅HentaiFeet VIP👣',
      callback_data='Hent_feet_button_pressed'
)

Footfet_button = InlineKeyboardButton(  #FF BUTTON
    text='🦶FootFetish VIP🦶',
    callback_data='ffvip_button_pressed'
)

b_t_s_button = InlineKeyboardButton(
    text='Back',
    callback_data='back_to_start_button_pressed'
)
b_t_s_button_after_admin = InlineKeyboardButton(
    text='Back',
    callback_data='b_t_s_button_after_admin'
)
catalog_button = InlineKeyboardButton(
    text='🔞Our VIP Channels🔞',
    callback_data='catalog_button_pressed'
)

admin_button = InlineKeyboardButton(
    text='Communication with the administration',
    callback_data='admin_button_pressed'
)

b_t_s_button_ifphoto = InlineKeyboardButton(
    text='Back',
    callback_data='b_t_s_button_ifphoto_pressed'
)

check_channels_button = InlineKeyboardButton(
       text='🔥GET FREE 18+ CONTENT🔥',
       callback_data='check_channels_button_pressed'
)



stars_pay = InlineKeyboardButton(
      text='Pay with stars⭐',
      callback_data='stars_pay_pressed'
)


catalog_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[catalog_button],
                    [check_channels_button],
                    [predlozhka_button],
                    [channels_button],
                    [admin_button]]
)
back_to_start_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
        [channels_button],
        [b_t_s_button]]
)
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[Footfet_button],
                    [Hent_feet_button],
                    [channels_button],
                    [b_t_s_button]
                    ]
)
check_sub_key = InlineKeyboardMarkup(
       inline_keyboard=[
              [check_sub_button]
       ]
)
b_t_s_keyboard_ifphoto = InlineKeyboardMarkup(
    inline_keyboard=[
        [oplata_button],
        [channels_button],
        [b_t_s_button_ifphoto]
    ]
)
b_t_s_keyboard_ifphoto_hentai = InlineKeyboardMarkup(
    inline_keyboard=[
        [stars_pay],
        [channels_button],
        [b_t_s_button_ifphoto]
    ]
)



method_oplata_hent = InlineKeyboardMarkup(
       inline_keyboard=[[stars_pay]     
       ]
)


