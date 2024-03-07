module.exports = {
    name: 'ban',
    category: 'Moderation',
    description: "This command bans a member!",
    
    execute(client, message, args, Discord){

        if(message.member.permissions.has("BAN_MEMBERS")){

            const member = message.mentions.users.first();
            if(!member){
                return message.reply("Please mention a valid member of the server")   
            }
            
            const memberTarget = message.guild.members.cache.get(member.id);


            let banReason = args.join("").slice(22);
            if (!banReason) {
                banReason = "None"
            }

            memberTarget.ban({
                reason: banReason,
                days: 0
            })
            message.channel.send(`${memberTarget} has been banned`)

        }else{
            message.channel.send('You do not have permission to use this command')
        }
        

    }
}