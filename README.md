<div align="center">
  <p>
    <a align="center" href="https://geno.my.canva.site/promraw" target="https://geno.my.canva.site/promraw">
      <img
        width="100%"
        src="https://github.com/mayuras7685/Prom-raw/blob/master/assets/Promdraw-v2.png"
      >
    </a>
  </p>



[How it works](https://github.com/mayuras7685/Prom-raw/tree/master?tab=readme-ov-file#how-it-works) | [Progress](https://github.com/mayuras7685/Prom-raw/tree/master?tab=readme-ov-file#-progress) | [IRL](https://github.com/mayuras7685/Prom-raw/tree/master?tab=readme-ov-file#-real-life-scenario-for-promraw) | [Prompts](https://github.com/mayuras7685/Prom-raw/tree/master?tab=readme-ov-file#%EF%B8%8F-how-we-generate-prompts) | [zkSync](https://github.com/mayuras7685/Prom-raw/tree/master?tab=readme-ov-file#-how-we-integrating-zksync)
</div>

## 👋 hello

Welcome to Promraw, an online game that brings together creativity and AI to score user-submitted digital drawings based on zany prompts! With Promraw, users can unleash their artistic talents while enjoying a fun and interactive experience.

<span><br></span>
## 🎯 Vision

Promraw aims to revolutionize the intersection of creativity, technology, and gaming by offering users a platform where they can unleash their imagination through digital drawing while leveraging AI for scoring and blockchain technology for ownership and monetization. The vision is to create an engaging and entertaining experience that empowers users to express themselves creatively, earn rewards for their participation, and contribute to a vibrant community of artists and gamers.

<span><br></span>
## 🥪 An AI Sandwich

with Humans in the Middle At a high level, **Promraw** flows the following way:

```bash
1.  A user sees a silly prompt to draw
```

```bash
2.  The user draws that prompt
```

```bash
3.  AI model scores that user's drawing and assigns a ranking
```

<span><br></span>
## 🔥How it works?

🤪 **Silly Prompts:** Users are presented with amusing and quirky prompts such as "a shark in a barrel" or "the world's fastest frog."

🖌️ **Drawing Time:** Users then draw their interpretation of the given prompt using our browser-based drawing tool.

🤖 **AI Scoring:** Once the drawing is submitted, our AI system, Paint, scores the drawing using CLIP, a model trained on image-text pairs. The closer the user's drawing is to the prompt's image representation according to CLIP, the higher the score.

<span><br></span>
## ⌨️ How We Generate Prompts?

We didn't stop at just a few prompts; we used AI to generate thousands of creative prompts! Here's how:

- **Initial Prompts**: We started with a set of initial prompts.
- **AI Prompt Generation**: Leveraging GPT-2, a generative text model, we expanded our prompt collection to include thousands of unique and unexpected ideas.
- **Human Touch**: While AI generated most of the prompts, our team ensured that they all encouraged fun and creativity.

<span><br></span>
## 🌐⛓️ Some extra sparkle from Blockchain/Web3:

- 🖼️ **Non-Fungible Tokens (NFTs):** Users can convert their submitted drawings into NFTs, representing unique digital assets that can be bought, sold, and traded on a marketplace. Each drawing could be minted as a separate NFT, enabling users to monetize their creativity and potentially earn rewards for high-scoring submissions.
- 💰**Tokenized Rewards:** Users are rewarded with tokens or cryptocurrency for participating in the game, submitting drawings, or achieving high scores.
- 🏠 **Private room:** With this feature, users can create exclusive drawing sessions where only those with the room link or code can participate just like Scribble.
- 🏆 **Community Challenges and Tournaments:** Organize tournaments where users compete to create the best drawings based on specific themes, with winners receiving rare NFTs or valuable rewards.

<span><br></span>
## 🏢 Real-life scenario for Promraw:

InnovateTech, a leading technology company specializing in cutting-edge software solutions, is gearing up for a rebranding initiative to reflect its commitment to innovation and creativity. As part of this rebranding effort, the company decides to host a `logo redesign competition` on `Promraw` to harness the creative talents of `artists and designers` worldwide.

<span><br></span>
## 🔁 Why zkSync?

zkSync is a Layer 2 scaling solution for Ethereum that uses zk-rollups to increase transaction throughput and reduce costs while maintaining the security and decentralization of Ethereum. It allows for fast and cheap transactions, which is essential for applications like Promraw that may involve numerous microtransactions for minting NFTs, rewarding users, and trading.

<span><br></span>
## 🔁 How we integrating zkSync?

- **Wallet and Account Management:** Create and manage zkSync wallets for users. Users will need to deposit ETH or ERC20 tokens from Ethereum to zkSync.
- **Deposit Funds:** Allow users to deposit funds from Ethereum to zkSync.
- **Minting NFTs:** NFT minting functionality using zkSync's contracts. zkSync supports ERC721 tokens, so you can deploy and interact with your NFT contracts similarly to Ethereum.
- **Withdraw Funds:** Allow users to withdraw funds from zkSync back to Ethereum.

<span><br></span>
## ⌛ Progress:
- [x] [V0: Demonstrated prompt - image similarity using CLIP (Webcam stream)](https://github.com/mayuras7685/Prom-raw/tree/master/V0)
- [x] [V1: Similarity matching with many images (Webapp)](https://github.com/mayuras7685/Prom-raw/tree/master/V1)
- [ ] V2: Paint webapp using React (Webapp)
- [ ] V3: zkSync integration for `NFT minting` & `transactions`
- [ ] Many more... 



<span><br></span>

> **P.S :** By investing in Promraw, you're not only supporting the development of a cutting-edge product but also tapping into the potential of a thriving community of artists, gamers, streamers and Content creators. Join us in shaping the future of digital creativity and gaming!

## © license

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
