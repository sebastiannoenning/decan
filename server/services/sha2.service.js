const crypto = require('crypto');
const hash = crypto.createHash('sha256');

const sha2Service = () => {
    const password = (user) => {
        const h = hash.update(password);
        console.log(h.digest('hex'))
        return h
    }
};