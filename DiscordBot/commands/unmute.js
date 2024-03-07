module.exports = {
    name: 'unmute',
    category: "Moderation",
    description: "This command unmutes a member",
    execute(client, message, args, Discord) {
        const target = message.mentions.users.first();

        if(!target){
            return message.reply("Please mention a valid member of the server");
        }

        let muteRole = message.guild.roles.cache.find(role => role.name === 'Muted')
        if (!muteRole){
            return message.reply("There is no Muted role on this server");
        }

        let memberTarget = message.guild.members.cache.get(target.id);
        memberTarget.roles.remove(muteRole.id);
        message.channel.send(`<@${memberTarget.user.id}> has been unmuted`)
    
    }
}