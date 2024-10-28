from telethon import TelegramClient, functions, types

# Your credentials
api_id = 24203730  # Your API ID
api_hash = '6efa22ef91ea3b662fc84e7e1e3988cc'  # Your API Hash
phone_number = '+918328275956'  # Your phone number

client = TelegramClient('report_session', api_id, api_hash)

async def main():
    # Link to the channel you want to report
    channel_link = 'https://t.me/+mj0ZVz0mxLE2NWFh'  # Replace with the actual channel link

    try:
        # Get the channel entity
        channel = await client.get_entity(channel_link)

        # Report the channel for child abuse
        await client(functions.messages.ReportRequest(
            peer=channel,
            id=[],  # You can leave this empty
            reason=types.InputReportReasonChildAbuse(),  # Reporting reason for child abuse
            message="This channel contains content related to child abuse."
        ))

        print("Channel reported successfully for child abuse.")
    except Exception as e:
        print("Error reporting the channel:", e)

with client:
    client.loop.run_until_complete(main())