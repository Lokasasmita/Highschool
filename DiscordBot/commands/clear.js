module.exports = {
    name: 'clear',
    aliases: ['purge'],
    description: "Clears a set amount of messages",
    async execute(client, message, cmd, args, Discord) {
        if(message.member.permissions.has("MANAGE_CHANNELS")){
            if(!args[0]) return message.reply("please enter the amount of messages that you want to clear!");
            if(isNaN(args[0])) return message.reply("please enter a real number!");
    
            if(args[0] > 100) return message.reply("You cannot delete more than 100 messages!")
            if(args[0] < 1) return message.reply("You must delete at least 1 message")
    
            await message.channel.messages.fetch({limit: ++args[0]}).then(messages =>{
                message.channel.bulkDelete(messages);
            });
        }else {
            message.channel.send("You do not have permissions to use this command")
        }

     
    }
}