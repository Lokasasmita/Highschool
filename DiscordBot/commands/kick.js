module.exports = {
    name: 'kick',
    category: 'Moderation',
    description: "This command kicks a member!",

    execute(client, message, args, Discord){
        
        if(message.member.permissions.has("KICK_MEMBERS")){

            const member = message.mentions.users.first();
            if(!member){
                return message.reply("Please mention a valid member of the server")   
            }
            
            const memberTarget = message.guild.members.cache.get(member.id);


            let kickReason = args.join("").slice(22);
            if (!kickReason) {
                kickReason = "None"
            }

            memberTarget.kick(kickReason)
            message.channel.send(`${memberTarget} has been kicked`)
         
            
        }else{
            message.channel.send('You do not have permission to use this command')
        }
        

    }
}