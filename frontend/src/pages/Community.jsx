import React, { useState } from 'react';
import { useTranslation } from 'react-i18next';
import { MessageSquare, ThumbsUp, Share2, Search, PlusCircle, User, Clock } from 'lucide-react';

const initialPosts = [
  {
    id: 1,
    author: "Ramesh Kumar",
    avatar: "RK",
    role: "Expert Farmer",
    time: "2 hours ago",
    title: "Best natural remedies for Tomato Early Blight in humid seasons?",
    content: "I've been dealing with early blight on my tomato crop this monsoon. I prefer organic methods over heavy chemicals. Has anyone had success with neem oil or any specific compost teas?",
    likes: 24,
    comments: 8,
    tags: ["Tomato", "Organic", "Disease Control"]
  },
  {
    id: 2,
    author: "Sita Devi",
    avatar: "SD",
    role: "Community Member",
    time: "5 hours ago",
    title: "Looking for local vendors for high-quality urea in Pune district",
    content: "Can anyone recommend a reliable agro-center near Pune? The last batch I bought was clumped and ineffective. Willing to travel a bit for a trusted supplier.",
    likes: 12,
    comments: 3,
    tags: ["Fertilizers", "Pune", "Vendor Recommendations"]
  },
  {
    id: 3,
    author: "AgroTech Expert",
    avatar: "AE",
    role: "Verified Agronomist",
    time: "1 day ago",
    title: "Warning: High humidity approaching. Prepare for fungal risks.",
    content: "The upcoming weather system shows sustained humidity above 85% for the next 3 days. This is prime condition for rust and blight. Make sure your drainage is clear and consider preventative sprays if your crop is vulnerable.",
    likes: 89,
    comments: 15,
    tags: ["Weather Alert", "Prevention", "Expert Advice"]
  }
];

const Community = () => {
  const { t } = useTranslation();
  const [posts, setPosts] = useState(initialPosts);
  const [newPost, setNewPost] = useState("");
  const [searchQuery, setSearchQuery] = useState("");

  const handlePostSubmit = (e) => {
    e.preventDefault();
    if (!newPost.trim()) return;

    const post = {
      id: Date.now(),
      author: "Current User",
      avatar: "CU",
      role: "Member",
      time: "Just now",
      title: "New Discussion",
      content: newPost,
      likes: 0,
      comments: 0,
      tags: ["General"]
    };

    setPosts([post, ...posts]);
    setNewPost("");
  };

  const filteredPosts = posts.filter(post => 
    post.title.toLowerCase().includes(searchQuery.toLowerCase()) || 
    post.content.toLowerCase().includes(searchQuery.toLowerCase()) ||
    post.tags.some(tag => tag.toLowerCase().includes(searchQuery.toLowerCase()))
  );

  return (
    <div className="max-w-5xl mx-auto space-y-8 animate-in fade-in duration-500 pb-12">
      {/* Header section */}
      <div className="mb-8 border-l-4 border-l-emerald-500 pl-4">
        <h1 className="text-3xl font-extrabold text-gray-900 border-b-2 border-transparent pb-1 inline-block flex items-center gap-3">
          Farmer Community Forum
          <span className="bg-emerald-100 text-emerald-700 text-xs px-2 py-1 rounded-full font-bold uppercase tracking-wider">Demo Access</span>
        </h1>
        <p className="text-gray-500 mt-2 text-lg">
          Ask questions, share advice, and connect with other farmers in your region.
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        
        {/* Main Feed */}
        <div className="lg:col-span-2 space-y-6">
          
          {/* Create Post Card */}
          <div className="bg-white rounded-3xl p-6 shadow-sm border border-gray-100">
            <h3 className="font-bold text-gray-800 mb-4 flex items-center gap-2">
              <PlusCircle className="w-5 h-5 text-emerald-600" /> Start a Discussion
            </h3>
            <form onSubmit={handlePostSubmit}>
              <textarea
                value={newPost}
                onChange={(e) => setNewPost(e.target.value)}
                placeholder="What's on your mind? Ask the community..."
                className="w-full bg-gray-50 border-2 border-transparent focus:border-emerald-500 focus:bg-white rounded-2xl p-4 transition-all resize-none h-28 text-gray-700"
              />
              <div className="flex justify-between items-center mt-4">
                <div className="text-sm text-gray-400 font-medium px-2">
                  Guidelines: Be respectful and helpful.
                </div>
                <button 
                  type="submit"
                  disabled={!newPost.trim()}
                  className="bg-emerald-600 hover:bg-emerald-700 text-white font-bold px-6 py-2.5 rounded-xl transition-all shadow-md shadow-emerald-200 disabled:opacity-50 disabled:hover:translate-y-0 hover:-translate-y-0.5"
                >
                  Post
                </button>
              </div>
            </form>
          </div>

          {/* Feed Controls */}
          <div className="flex flex-col sm:flex-row gap-4 items-center justify-between">
            <div className="relative w-full sm:w-auto flex-1 max-w-md">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
              <input 
                type="text" 
                placeholder="Search discussions near you..." 
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full bg-white border border-gray-200 focus:border-emerald-500 rounded-full py-2.5 pl-10 pr-4 outline-none transition-colors"
              />
            </div>
            <div className="flex gap-2">
              <select className="bg-white border border-gray-200 rounded-full px-4 py-2.5 text-sm font-medium text-gray-700 outline-none focus:border-emerald-500">
                <option>Recent</option>
                <option>Most Helpful</option>
                <option>My Crops</option>
              </select>
            </div>
          </div>

          {/* Posts List */}
          <div className="space-y-6">
            {filteredPosts.length > 0 ? (
              filteredPosts.map(post => (
                <div key={post.id} className="bg-white rounded-3xl p-6 shadow-sm border border-gray-100 hover:border-emerald-100 transition-colors">
                  
                  {/* Post Header */}
                  <div className="flex justify-between items-start mb-4">
                    <div className="flex items-center gap-3">
                      <div className="w-12 h-12 rounded-full bg-gradient-to-br from-emerald-400 to-teal-500 flex items-center justify-center text-white font-bold text-lg shadow-inner">
                        {post.avatar}
                      </div>
                      <div>
                        <h4 className="font-bold text-gray-900">{post.author}</h4>
                        <div className="flex items-center gap-2 text-xs text-gray-500">
                          <span className={`px-2 py-0.5 rounded-full font-medium ${post.role.includes('Expert') || post.role.includes('Agronomist') ? 'bg-blue-50 text-blue-600' : 'bg-gray-100'}`}>
                            {post.role}
                          </span>
                          •
                          <span className="flex items-center gap-1"><Clock className="w-3 h-3"/> {post.time}</span>
                        </div>
                      </div>
                    </div>
                  </div>

                  {/* Post Content */}
                  <div>
                    <h2 className="text-xl font-bold text-gray-900 mb-2">{post.title}</h2>
                    <p className="text-gray-600 leading-relaxed mb-4">
                      {post.content}
                    </p>
                    
                    {/* Tags */}
                    <div className="flex flex-wrap gap-2 mb-6">
                      {post.tags.map((tag, idx) => (
                        <span key={idx} className="text-xs font-bold px-3 py-1 bg-gray-50 text-gray-600 rounded-lg border border-gray-100">
                          #{tag.replace(/\s+/g, '')}
                        </span>
                      ))}
                    </div>
                  </div>

                  {/* Post Actions */}
                  <div className="flex items-center gap-6 pt-4 border-t border-gray-100">
                    <button className="flex items-center gap-2 text-gray-500 hover:text-emerald-600 transition-colors font-medium text-sm">
                      <ThumbsUp className="w-5 h-5" /> 
                      <span>{post.likes} Helpful</span>
                    </button>
                    <button className="flex items-center gap-2 text-gray-500 hover:text-blue-600 transition-colors font-medium text-sm">
                      <MessageSquare className="w-5 h-5" /> 
                      <span>{post.comments} Replies</span>
                    </button>
                    <button className="flex items-center gap-2 text-gray-500 hover:text-gray-900 transition-colors font-medium text-sm ml-auto">
                      <Share2 className="w-5 h-5" /> 
                      <span>Share</span>
                    </button>
                  </div>
                </div>
              ))
            ) : (
              <div className="text-center py-12 text-gray-500">
                <Search className="w-12 h-12 mx-auto text-gray-300 mb-4" />
                <p>No discussions found matching "{searchQuery}"</p>
              </div>
            )}
          </div>
        </div>

        {/* Sidebar */}
        <div className="space-y-6 hidden lg:block">
          {/* Trending Topics */}
          <div className="bg-white rounded-3xl p-6 shadow-sm border border-gray-100">
            <h3 className="font-bold text-gray-900 mb-4 flex items-center gap-2">
              Trending Topics
            </h3>
            <div className="space-y-4">
              {[
                { tag: "MonsoonPrep", count: 124 },
                { tag: "OrganicFertilizers", count: 98 },
                { tag: "PestControl", count: 85 },
                { tag: "GovSubsidy", count: 64 },
                { tag: "TomatoPrices", count: 42 }
              ].map((topic, i) => (
                <div key={i} className="flex justify-between items-center group cursor-pointer">
                  <span className="text-gray-600 font-medium group-hover:text-emerald-600 transition-colors">#{topic.tag}</span>
                  <span className="text-xs font-bold text-gray-400 bg-gray-50 px-2 py-1 rounded-md">{topic.count}</span>
                </div>
              ))}
            </div>
          </div>

          {/* Top Contributors */}
          <div className="bg-white rounded-3xl p-6 shadow-sm border border-gray-100">
            <h3 className="font-bold text-gray-900 mb-4 flex items-center gap-2">
              Top Contributors
            </h3>
            <div className="space-y-4">
              {[
                { name: "Dr. Anil Sharma", detail: "Agronomist • 2.4k Helpful" },
                { name: "Ramesh Kumar", detail: "Expert Farmer • 1.1k Helpful" },
                { name: "Kisan Center", detail: "Verified Vendor • 840 Helpful" }
              ].map((user, i) => (
                <div key={i} className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-full bg-gray-100 flex items-center justify-center text-gray-500">
                    <User className="w-5 h-5" />
                  </div>
                  <div>
                    <div className="font-bold text-sm text-gray-900">{user.name}</div>
                    <div className="text-xs text-gray-500">{user.detail}</div>
                  </div>
                </div>
              ))}
            </div>
            <button className="w-full mt-6 py-2 border-2 border-emerald-100 hover:border-emerald-200 text-emerald-700 rounded-xl font-bold text-sm transition-colors">
              View All Experts
            </button>
          </div>
        </div>

      </div>
    </div>
  );
};

export default Community;
